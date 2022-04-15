# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> activeObj
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-04 14:50
    @Desc   :活动人对象

-------------------------------------------------
   Change Activity:
                   2022-03-04 14:50:
-------------------------------------------------
"""
__author__ = 'bobi'

import math
import queue
import random
import time


class activeObj:
    """活动人对象"""

    def __init__(self, legs, file):
        self.activeID = self.generatePID()
        # 记录构成人的两个腿部特征点对象
        # 其类型为列表
        self.legs = legs
        # 两个特征点的运动信息跟踪
        self.targetTracking = ([legs[0].position], [legs[1].position])
        self.lastUpdateTime = self.getTime()
        self.recentID = 1
        self.file = file

    # 为特征点生成唯一的ID
    def generatePID(self):
        tim = time.time()  # 获取Python时间戳
        tim = tim * 1000  # 转Java时间戳
        tim = str(tim)
        # print(tim)
        # ts时间戳
        ts = tim.split('.')[0]
        ran = random.randint(100, 999)
        ran = str(ran)
        # reqId时间戳拼接随机数
        reqId = ts + ran
        # print(reqId)
        return reqId

    # 该函数用于向该活动人添加跟踪信息
    def addANDUpdateTrack(self, keyPoint):
        print("运动信息存储,当前活动人为:", self.activeID, file=self.file)
        print("原来运动信息[0]为", self.targetTracking[0], file=self.file)
        print("原来运动信息[1]为", self.targetTracking[1], file=self.file)
        # 首先判断该点keyPoint属于哪一只脚
        idx = 0 if keyPoint.keyPID == self.legs[0].keyPID else 1

        print("此时idx：", idx, "  上次更新的脚recentID:", self.recentID, file=self.file)

        diffFrames = (keyPoint.ownFrames - self.legs[self.recentID].ownFrames)
        print("上次更新的周期为", self.legs[self.recentID].ownFrames, "    当前更新点与上一次的更新帧数差为：", diffFrames, file=self.file)
        tempidx = 1 if idx == 0 else 0
        # 再根据idx将特征点记录
        if idx != self.recentID:
            if idx == 1:
                while diffFrames > 0:
                    self.targetTracking[idx].append(None)
                    self.targetTracking[tempidx].append(None)
                    diffFrames -= 1
                self.targetTracking[idx].append(keyPoint.position)
            else:
                diffFrames -= 1
                while diffFrames > 0:
                    self.targetTracking[idx].append(None)
                    self.targetTracking[tempidx].append(None)
                    diffFrames -= 1
                self.targetTracking[idx].append(keyPoint.position)
                pass
        else:
            print("缺少一另一只脚的信息，该活动人更新同一只脚的信息(补一个none)", file=self.file)
            diffFrames -= 1
            while diffFrames > 0:
                self.targetTracking[idx].append(None)
                self.targetTracking[tempidx].append(None)
                diffFrames -= 1
            self.targetTracking[tempidx].append(None)
            self.targetTracking[idx].append(keyPoint.position)

        self.recentID = idx
        print("更新结束tempID更新为:", self.recentID, file=self.file)
        print("targetTracking的内容", file=self.file)
        print("此时运动信息[0]为", self.targetTracking[0], file=self.file)
        print("此时运动信息[1]为", self.targetTracking[1], file=self.file)
        self.legs[idx].ownFrames = keyPoint.ownFrames

        # 更新有效时间
        self.lastUpdateTime = self.getTime()

    # 获取当前时间戳
    def getTime(self):
        tim = time.time() * 100  # 获取Python时间戳
        tim = math.floor(tim)
        return tim
