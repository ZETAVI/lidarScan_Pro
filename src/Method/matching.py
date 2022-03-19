# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> matching
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-03 15:48
    @Desc   :拟合与特征提取
            负责计算动态窗口聚类objectQueue点集的拟合度(R_Squared)
            返回符合条件的特征点T 维护队列keyPoints
-------------------------------------------------
   Change Activity:
                   2022-03-03 15:48:
-------------------------------------------------
"""
__author__ = 'bobi'

import threading
import src.Method.globalFunc as Fun
from src.Object import keyPoint


class matching:
    """聚类对象拟合与特征提取"""

    def __init__(self, objectQueue, keyPoints):
        # object点集
        self.objectQueue = objectQueue
        # 特征点集
        self.keyPoints = keyPoints
        threading.Thread(target=self.match, ).start()

    # 拟合线程
    def match(self):
        while True:
            if not self.objectQueue.empty():
                # 从objectQueue队列中取已经聚类好的object
                # object类型为元组
                object = self.objectQueue.get(block=True, timeout=1)

                # 具体实现思路：进行平移处理，然后判断是否符合人腿特征，符合的将其添加入特征点元组
                for tempObj in object:
                    x, y, middle_index = Fun.transform_matching(tempObj)
                    if Fun.judege(x, y):
                        # # 判断上一帧的特征点中是否有相近特征点 有的话就当场替换，没有就添加
                        # if matchingKeyPoint(tempObj[middle_index], self.keyPoints):
                        #     continue
                        # 如果初步符合特征,提取特征点
                        tempkeypoint = keyPoint(position=tempObj[middle_index])
                        # tempkeypoint.generatePID()
                        # tempkeypoint.setTime()
                        print("找到符合的特征点")
                        print(tempObj[middle_index].angle, tempObj[middle_index].range)

                        # 存入keyPoints队列后续处理
                        self.keyPoints.put(item=tempkeypoint, block=True, timeout=1)
                        # print(tempkeypoint)
