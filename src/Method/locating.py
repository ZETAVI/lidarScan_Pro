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

import threading
import time
import src.Method.globalFunc as Fun
from src.Object import activeObj


class locate_storage:
    """特征点定位与活动人存储"""

    def __init__(self, keyPoints, activeObjs, file):
        # 关键点集合(待处理)
        self.keyPoints = keyPoints
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
        self.file = file
        # 启动定位线程
        threading.Thread(target=self.locate()).start()

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

            print("开始定位!!!!!!!!!!!!!!!!!!!!!!", file=self.file)
            print("待处理点信息为:", file=self.file)
            keyPoint.infoPrint()
            # 取出点的最新帧数
            curFrame = keyPoint.ownFrames

            # 用于缓存所有可能的相邻帧
            neighbours = []
            print("在跟踪表中搜索可能的相邻点!!!!!!!!!!!!", file=self.file)
            print("跟踪表内共有:", len(self.trackList), "个跟踪信息!!!", file=self.file)
            # 在跟踪表中利用最邻近法定位
            for point in self.trackList:
                # 根据curTime清除跟踪表中过期的点
                tempFrame = curFrame
                print("当前比对点的信息:", file=self.file)
                point.infoPrint()
                # print("当前比对点的帧数：", curFrame)
                if tempFrame < point.ownFrames:
                    tempFrame += 9999999
                if tempFrame - point.ownFrames > 9:
                    # print("跟踪表中的点的信息：")
                    print("超过6帧没更新，该点从跟踪列表中删除", file=self.file)
                    self.trackList.remove(point)
                    continue
                # 加上了周期帧数判断
                dis = Fun.distanceXY(point.position, keyPoint.position)
                print("待处理点与跟踪点距离为:", dis, file=self.file)
                if curFrame != point.ownFrames and dis <= self.neighbour:
                    # 可能为相邻帧的点集
                    print("找到该点在跟踪表中的相近点!!!!!!!!!：", file=self.file)
                    neighbours.append(point)

            print("跟踪表搜索完成!!!!", file=self.file)
            # todo 输出所有找到的neighbours
            print("此时相近点集合neighbours：", file=self.file)
            for TempPoint in neighbours:
                TempPoint.infoPrint()

            # 若在跟踪标表中找不到对应点
            if len(neighbours) == 0:
                print("该点在跟踪表中无相近点，当前帧的点为", file=self.file)
                # 生成一个唯一的编号
                keyPoint.generatePID()
                print("生成一个该点的唯一编号，并将其放入跟踪表中", file=self.file)
                keyPoint.infoPrint()
                # 更新跟踪表
                self.trackList.append(keyPoint)
                # 申请存储该特征点
                self.store(keyPoint)
                continue

            # 定位到上个周期的最匹配对应点matched
            if len(neighbours) > 1:
                # 跟踪表中有找到一只以上的对应点
                print("该点在跟踪表中有找到一只以上的对应点，找出最适合的点", file=self.file)
                matched = self.movementTrendCHK(neighbours=neighbours, cur=keyPoint)

            else:
                print("该点在跟踪表中只有一只对应点", file=self.file)
                matched = neighbours[0]
            print("此时跟踪列表中最适合的对应点为：", file=self.file)
            matched.infoPrint()

            # 判断这个点是否能构成活动人对象,即是否能在字典中找到该点ID对应的活动人ID
            keyPoint.keyPID = matched.keyPID
            if self.point2obj.__contains__(keyPoint.keyPID):
                print("该点在跟踪表中,也在活动人表中，更新相应的信息", file=self.file)
                curActiveObj = self.point2obj[keyPoint.keyPID]
                # 加入该活动人对应位置,并自动更新活动人的有效时间
                curActiveObj.addANDUpdateTrack(keyPoint=keyPoint)
                # 更新跟踪表
                matched.update(keyPoint, curFrame)
                print("跟踪表中的对应点的信息更新 ,更新后为", file=self.file)
                matched.infoPrint()

            # 该点在跟踪表中,但是不在活动人表中,说明该点在上个周期还不能构造出一个人
            else:
                print("该点在跟踪表中,但是不在活动人表，将该点放入等待空间", file=self.file)
                print("跟踪表中的对应点的信息更新，同时将该点放入等待空间，等待下一个点使之能聚成活动人对象", file=self.file)
                # 更新跟踪表
                matched.update(keyPoint, curFrame)
                # 申请存储
                if self.store(keyPoint) == 1:
                    matched.vector = None

    # todo 申请存储方法 利用等待空间
    def store(self, curPoint):
        curPoint.infoPrint()
        print("该点尝试存储", file=self.file)
        # 若等待空间为空 申请一个等待空间存放当前点
        if self.waitArea is None:
            print("等待空间为空,初始化等待空间", file=self.file)
            self.waitArea = waitingArea(curPoint, file=self.file)
        else:
            # 若等待空间非空 则检测两点是否超时  超时返回空 否则返回活动人对象
            newActiveObj = self.waitArea.checkDistanceOut(curPoint)
            if newActiveObj is not None:
                # 添加到活动人队列中
                print("构造出新的活动人!!!!! 加入活动人队列", file=self.file)
                self.activeObjs.put(item=newActiveObj, block=True, timeout=1)
                print("此次放入字典的两脚：", file=self.file)
                print("脚1：", file=self.file)
                newActiveObj.legs[0].infoPrint()
                print("脚2：", file=self.file)
                newActiveObj.legs[1].infoPrint()

                # 更新两特征点与活动人对应的字典
                self.point2obj[newActiveObj.legs[0].keyPID] = newActiveObj
                self.point2obj[newActiveObj.legs[1].keyPID] = newActiveObj
                print("此时特征点与活动人对应的字典内容为：", file=self.file)
                for key in self.point2obj.keys():
                    print("key：", key, "value：", self.point2obj[key].activeID, file=self.file)
                return 1
        return 0

    # todo 根据运动趋势匹配最符合的点
    def movementTrendCHK(self, neighbours, cur):
        print("运动趋势匹配开始,共有neighbours:", len(neighbours), "个", file=self.file)
        # 记录最短距离
        minDis = 99999
        # 记录最小角度
        minAng = 360
        temp = None
        ans = None
        for point in neighbours:
            print("正在处理neighbour:", point.keyPID, file=self.file)
            dis = Fun.distanceXY(point.position, cur.position)
            print("该neighbour与cur 距离为:", dis, file=self.file)
            if dis < 0.1:
                return point
            if dis < minDis:
                ans = point
                minDis = dis
            if point.vector is None:
                print("neighbour:", point.keyPID, "的运动趋势vector为空", file=self.file)
                continue

            trend = Fun.distanceXY(point.vector, point.position)
            print("neighbour:", point.keyPID, "运动趋势vector距离为", trend, file=self.file)
            # trend 记录运动趋势 若运动幅度较小 误差考虑忽略
            if trend < 0.01:
                print("trend过小跳过", file=self.file)
                continue
            else:
                x = [cur.position[0], point.vector[0], point.position[0]]
                y = [cur.position[1], point.vector[1], point.position[1]]

                # 计算角度偏差
                print("x: ", x, file=self.file)
                print("y: ", y, file=self.file)
                deviation = Fun.angle_calculate(x, y, 0, 1, 2)
                print("neighbour:", point.keyPID, "运动趋势vector的偏移角度为", deviation, file=self.file)
                # 夹角小于30度
                if deviation < 15 and deviation < minAng:
                    print("小于15且小于最小偏角 替换定位点", file=self.file)
                    minAng = deviation
                    temp = point

        return ans if temp is None else temp


class waitingArea:
    """等待空间"""

    # 用一个特征点初始化等待空间
    def __init__(self, waitPoint, file):
        # 记录阻塞特征点
        self.waitPoint = waitPoint
        self.file = file
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
        if self.waitPoint is None or self.waitPoint.keyPID == newPoint.keyPID:
            self.waitPoint = newPoint
            return None
        else:
            print("等待空间非空, 等待空间存储的点为", file=self.file)
            self.waitPoint.infoPrint()
            # 若无超距离 则两个特征点能构成一个活动人 构造活动人 返回新的活动人对象
            dis = Fun.distanceXY(self.waitPoint.position, newPoint.position)
            print("等待空间两点距离为", dis, file=self.file)
            if 0.35 > dis > 0.1:
                print("等待空间两点距离小于0.35 可以构成活动人", file=self.file)
                newObj = activeObj(legs=[self.waitPoint, newPoint], file=self.file)
                self.waitPoint = None
                return newObj
            else:
                # 若已超距 更新等待空间
                print("等待空间两点距离过大 更新等待空间", file=self.file)
                self.waitPoint = newPoint
                return None
