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

from src.Object import keyPoint, activeObj


class locate_storage:
    """特征点定位与活动人存储"""

    def __init__(self, keyPoints, flag, activeObjs):
        keyPoints = queue.Queue
        # 关键点集合(待处理)
        self.keyPoints = keyPoints
        self.flag = flag
        # 活动人对象集合
        self.activeObjs = activeObjs
        # 跟踪表
        self.trackList = []
        # 对应字典  关键点对应到活动人ID
        self.point2obj = {}
        # todo 跟踪表超时设置
        # self.timeout=?
        # todo 两点邻域阈值
        # self.neighbour=?
        # 等待空间 需要使用是才创建,使用完毕后清除
        self.waitArea = None
        # 启动定位线程
        # threading.Thread(target=self.locate())

    def locate(self):
        while self.flag:
            if not self.keyPoints.empty():
                # 取新周期的关键点
                keyPoint = self.keyPoints.get(block=True, timeout=1)
                # curTime 类型为int 表示时间戳
                curTime = keyPoint.setTime()

                # todo 根据curTime清除跟踪表中过期的点
                for point in self.trackList:
                    if curTime - point.time > self.timeout:
                        pass

                # 标记是否能在跟踪表中找到对应点
                alreadyProcess = False

                # todo 在跟踪表中利用最邻近法定位
                for point in self.trackList:
                    if self.distance(point, keyPoint) <= self.neighbour:
                        alreadyProcess = True
                        # 定位到上个周期的对应点
                        # 判断这个点是否能构成活动人对象,即是否能在字典中找到该点ID对应的活动人ID
                        keyPoint.keyPID = point.keyPID
                        if self.point2obj.__contains__(keyPoint.keyPID):
                            # todo 加入该活动人对应位置,并自动更新活动人的有效时间
                            activeObj = self.point2obj[keyPoint.keyPID]
                            activeObj.addANDUpdateTrack(keyPoint=keyPoint)

                            # 更新跟踪表
                            point.update(keyPoint)
                            pass

                        # 该点在跟踪表中,但是不在活动人表中,说明该点在上个周期还不能构造出一个人
                        else:
                            # 更新跟踪表
                            point.update(keyPoint)
                            # 申请存储
                            self.store(keyPoint)

                # 若在跟踪标表中找不到对应点
                if not alreadyProcess:
                    # 生成一个唯一的编号
                    keyPoint.generatePID()
                    # 更新跟踪表
                    self.trackList.append(keyPoint)
                    # 申请存储该特征点
                    self.store(keyPoint)

    # todo 申请存储方法 利用等待空间
    def store(self, curPoint):
        # 若等待空间为空 申请一个等待空间存放当前点
        if self.waitArea is None:
            self.waitArea = waitingArea(curPoint)
        else:
            # 若等待空间非空 则检测两点是否超时  超时返回空 否则返回活动人对象
            activeObj = self.waitArea.checkTimeOut(curPoint)
            if activeObj is not None:
                # 更新两特征点与活动人对应的字典
                self.point2obj[activeObj.legs[0].keyPID] = activeObj.activeID
                self.point2obj[activeObj.legs[1].keyPID] = activeObj.activeID

    # todo 计算两点的欧拉公式
    def distance(self, pointA, pointB):
        dis = 0.0
        return dis


class waitingArea:
    """等待空间"""

    # 用一个特征点初始化等待空间
    def __init__(self, waitPoint):
        # 记录阻塞特征点
        self.waitPoint = waitPoint
        # 记录等待开始时间
        self.waitTime = self.setTime()
        # 最大的等待时间
        self.timeout = 1

    # 获取时间戳
    def setTime(self):
        tim = time.time() * 100  # 获取Python时间戳
        tim = math.floor(tim)
        return tim

    # 检测新的点是否能与等待空间中的点组成活动人
    def checkTimeOut(self, newPoint):
        # 若无超时 则两个特征点能构成一个活动人 构造活动人 返回新的活动人对象
        if newPoint.time - self.waitTime <= self.timeout:
            return activeObj(legs=(self.waitPoint, newPoint))
        else:
            # 若已超时 更新等待空间
            self.waitPoint = newPoint
            self.waitPoint = self.setTime()
            return None
