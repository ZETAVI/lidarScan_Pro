# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> keyPoint
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-03 21:32
    @Desc   :特征点类
-------------------------------------------------
   Change Activity:
                   2022-03-03 21:32:
-------------------------------------------------
"""
__author__ = 'bobi'

import math
import random
import time


class keyPoint:
    """特征点"""

    def __init__(self, position):
        self.ID = None
        self.position = position
        self.time = None

    # 为特征点生成唯一的ID
    def generateID(self):
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
        self.ID = reqId

    # 获取时间戳
    def getTime(self):
        tim = time.time() * 100  # 获取Python时间戳
        tim = str(math.floor(tim))
        self.time = tim

