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
import time


class matching:
    """聚类对象拟合与特征提取"""

    def __init__(self, objectQueue, keyPoints, showObjQueue2):
        # object点集
        self.objectQueue = objectQueue
        # 特征点集
        self.keyPoints = keyPoints
        # 结果点集
        self.showObjQueue2 = showObjQueue2
        threading.Thread(target=self.match, ).start()

    # 拟合线程
    def match(self):
        while True:

            # 从队头取元素 等待时间不能错过1秒
            # todo 第一步 从当聚类对象队列非空时中取出所有聚类目标
            objectsPeriod = None
            if not self.objectQueue.empty():
                objectsPeriod = self.objectQueue.get(block=True, timeout=1)
                print("取出成功")

            # 有可能取出失败
            if objectsPeriod is None:
                # print("队列为空")
                time.sleep(0.1)
                continue
            startTime = time.time()
            # while True:
            # 待显示的聚类对象的集合
            final = []
            # if not self.objectQueue.empty():
            # 从objectQueue队列中取已经聚类好的object
            # object类型为元组
            # object = self.objectQueue.get(block=True, timeout=1)
            # todo 第二步 处理取出的所有聚类目标
            # 具体实现思路：进行平移处理，然后判断是否符合人腿特征，符合的将其添加入特征点元组
            # print("2222")
            for tempObj in objectsPeriod:
                x, y, middle_index = Fun.transform_matching2(tempObj)
                if Fun.judege(x, y, middle_index):
                    # # 判断上一帧的特征点中是否有相近特征点 有的话就当场替换，没有就添加
                    # if matchingKeyPoint(tempObj[middle_index], self.keyPoints):
                    #     continue
                    # 如果初步符合特征,提取特征点
                    tempkeypoint = keyPoint(position=tempObj[middle_index])

                    # print("找到符合的特征点")
                    # print(tempObj[middle_index].angle, tempObj[middle_index].range)

                    # 将聚类对象添加入待显示对象队列
                    final.append(tempObj)

                    # 存入keyPoints队列等待后续处理
                    # self.keyPoints.put(item=tempkeypoint, block=True, timeout=1)
                    # print(tempkeypoint)

            # todo 第三步 将当前符合条件的所有聚类目标进行显示
            self.showObjQueue2.put(item=final, block=True, timeout=1)
            print("时间：", time.time() - startTime)
            # print(final)
