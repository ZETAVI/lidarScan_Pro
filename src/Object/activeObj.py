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

    def __init__(self, legs):
        self.activeID = self.generatePID()
        # 记录构成人的两个腿部特征点keyPID
        # 其类型为元组
        self.legs = legs
        # 两个特征点的运动信息跟踪
        self.targetTracking = ([], [])
        self.lastUpdateTime = self.getTime()

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
        # 首先判断该点keyPoint属于哪一只脚
        idx = 0 if keyPoint.keyPID == self.legs[0] else 1
        # 再根据idx将特征点记录
        self.targetTracking[idx].append(keyPoint)
        # 更新有效时间
        self.lastUpdateTime = self.getTime()

    # 获取当前时间戳
    def getTime(self):
        tim = time.time() * 100  # 获取Python时间戳
        tim = math.floor(tim)
        return tim
