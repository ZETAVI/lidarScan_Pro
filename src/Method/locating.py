# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> locating
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-04 10:22
    @Desc   :关键点定位线程
            维护跟踪表与活动目标表
            1.去除超时点
            2.特征点定位
                2.1 新出现的点 生成时间戳和ID后 添加到跟踪表中
                    活动人存储
                    加入到等待空间 或 判断是否能与等待空间内的关键点构成一个活动人
                    若能构建出一个活动人 则 创建字典记录关键点和活动人的对应关系
                2.2 发现临界点 取邻近点ID 生成新的时间戳后 更新跟踪表
                    根据字典找到该特征点对应的活动人对象 在对应位置存储
-------------------------------------------------
   Change Activity:
                   2022-03-04 10:22:
-------------------------------------------------
"""
__author__ = 'bobi'

import math
import queue
import threading
import time
import src.Method.globalFunc as Fun
from src.Object import activeObj


class locate_storage:
    """特征点定位与活动人存储"""

    def __init__(self, keyPoints, flag, activeObjs):
        # 关键点集合(待处理)
        self.keyPoints = keyPoints
        self.flag = flag
        # 活动人对象集合
        self.activeObjs = activeObjs
        # 跟踪表
        self.trackList = []
        # 对应字典  关键点对应到活动人ID
        self.point2obj = {}
        # todo 两点邻域阈值
        self.neighbour = 0.4
        # 等待空间 需要使用是才创建,使用完毕后清除
        self.waitArea = None
        # 启动定位线程
        # threading.Thread(target=self.locate())

    def locate(self):
        while True:
            keyPoint = None
            if not self.keyPoints.empty():
                # 取新周期的关键点
                keyPoint = self.keyPoints.get(block=True, timeout=1)

            # 有可能去除失败
            if keyPoint is None:
                time.sleep(0.05)
                continue

            # 取出点的最新帧数
            curFrame = keyPoint.ownFrames

            # 用于缓存所有可能的相邻帧
            neighbours = []
            # todo 在跟踪表中利用最邻近法定位
            for point in self.trackList:
                # todo 根据curTime清除跟踪表中过期的点
                tempFrame = curFrame
                print("当前最新点的帧数： ", curFrame)
                if tempFrame < point.ownFrames:
                    tempFrame += 9999999
                if tempFrame - point.ownFrames > 6:
                    print("点的信息：")
                    point.infoPrint()
                    print("超过6帧没更新，该点从跟踪列表中删除")
                    self.trackList.remove(point)
                    continue
                # todo 还要加上周期帧数判断
                if curFrame != point.ownFrames and Fun.distance(point.position,
                                                                keyPoint.position) <= self.neighbour:
                    # 可能为相邻帧的点集
                    print("找到该点在跟踪表中的相近点：")
                    print("当前帧的：")
                    keyPoint.infoPrint()
                    print("跟踪表中的点为：")
                    point.infoPrint()
                    neighbours.append(point)

            # 若在跟踪标表中找不到对应点
            if len(neighbours) == 0:
                print("该点在跟踪表中无相近点：")
                # 生成一个唯一的编号
                keyPoint.generatePID()
                # 更新跟踪表
                self.trackList.append(keyPoint)
                # 申请存储该特征点
                self.store(keyPoint)
                continue

            # 定位到上个周期的最匹配对应点matched
            if len(neighbours) > 1:
                # 跟踪表中有找到一只以上的对应点
                matched = self.movementTrendCHK(neighbours=neighbours, cur=keyPoint)
            else:
                matched = neighbours[0]

            # 判断这个点是否能构成活动人对象,即是否能在字典中找到该点ID对应的活动人ID
            keyPoint.keyPID = matched.keyPID
            if self.point2obj.__contains__(keyPoint.keyPID):
                curActiveObj = self.point2obj[keyPoint.keyPID]
                # todo 加入该活动人对应位置,并自动更新活动人的有效时间
                curActiveObj.addANDUpdateTrack(keyPoint=keyPoint)

                # 更新跟踪表
                matched.update(keyPoint, curFrame)

            # 该点在跟踪表中,但是不在活动人表中,说明该点在上个周期还不能构造出一个人
            else:
                # 更新跟踪表
                matched.update(keyPoint, curFrame)
                # 申请存储
                self.store(keyPoint)

    # todo 申请存储方法 利用等待空间
    def store(self, curPoint):
        curPoint.infoPrint()
        print("该点尝试继续存储")
        # 若等待空间为空 申请一个等待空间存放当前点
        if self.waitArea is None:
            self.waitArea = waitingArea(curPoint)
        else:
            # 若等待空间非空 则检测两点是否超时  超时返回空 否则返回活动人对象
            newActiveObj = self.waitArea.checkDistanceOut(curPoint)
            if newActiveObj is not None:
                # 添加到活动人队列中
                self.activeObjs.put(item=newActiveObj, block=True, timeout=1)
                # 更新两特征点与活动人对应的字典
                self.point2obj[newActiveObj.legs[0].keyPID] = newActiveObj
                self.point2obj[newActiveObj.legs[1].keyPID] = newActiveObj

    # todo 根据运动趋势匹配最符合的点
    def movementTrendCHK(self, neighbours, cur):
        # 记录最短距离
        minDis = 99999
        # 记录最小角度
        minAng = 360
        temp = None
        ans = None
        for point in neighbours:
            dis = Fun.distance(point.position, cur.position)
            if dis < minDis:
                ans = point
            if point.vector is None:
                continue

            trand = Fun.distance(point.vector.position, point.position)
            # trand 记录运动趋势 若运动幅度较小 误差考虑忽略
            if trand < 0.01:
                continue
            else:
                points = [cur.position, point.vector.position, point.position]
                x, y = Fun.transform_matching2(points)
                # 计算角度偏差
                deviation = Fun.angle_calculate(x, y, 0, 1, 2)
                # 夹角小于30度
                if deviation < 30 and deviation < minAng:
                    minAng = deviation
                    temp = point

        return ans if temp is None else temp


class waitingArea:
    """等待空间"""

    # 用一个特征点初始化等待空间
    def __init__(self, waitPoint):
        # 记录阻塞特征点
        self.waitPoint = waitPoint
        # 记录等待开始时间
        # self.waitTime = self.setTime()
        # 最大的等待时间
        # self.timeout = 1

    # 获取时间戳
    # def setTime(self):
    #     tim = time.time() * 100  # 获取Python时间戳
    #     tim = math.floor(tim)
    #     return tim

    # 检测新的点是否能与等待空间中的点组成活动人
    def checkDistanceOut(self, newPoint):
        # 若无超距离 则两个特征点能构成一个活动人 构造活动人 返回新的活动人对象
        if Fun.distance(self.waitPoint, newPoint) < 0.4:
            return activeObj(legs=(self.waitPoint, newPoint))
        else:
            # 若已超距 更新等待空间
            self.waitPoint = newPoint
            return None
