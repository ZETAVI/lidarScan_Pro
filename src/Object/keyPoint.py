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

import random
import time
import src.Method.globalFunc as Fun


class keyPoint:
    """特征点"""

    def __init__(self, position, frames):
        self.keyPID = None
        # 极坐标
        self.position = position
        # 运动趋势 记录上一个点
        self.vector = None
        # 用来统计帧数变化
        self.ownFrames = frames

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
        self.keyPID = reqId

    # 更新点信息
    def update(self, newState, newFrames):
        # vector 更新为上一帧位置信息
        self.vector = self.position
        self.position = newState.position
        self.ownFrames = newFrames

    def infoPrint(self):
        x, y = Fun.transform_clustering(self.position)
        vx, vy = None, None if self.vector is None else Fun.transform_clustering(self.vector)
        print("输出keyPoint点信息: ")
        print("    KID=", self.keyPID, "  ownFrames=", self.ownFrames)
        print("    position=", x, " ,  ", y, "    vector=", vx, " ,  ", vy)

# if __name__ == '__main__':
#     while 1:
#         start = keyPoint().setTime()
#         time.sleep(2)
#         curTime = math.floor(time.time() * 100)
#         print(curTime - start)
#         time.sleep(1)
