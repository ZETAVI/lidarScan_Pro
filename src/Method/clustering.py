# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> clustering
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-03 10:45
    @Desc   :聚类线程
            负责控制动态窗口与窗口点集聚类
            维护返回动态窗口聚类集合objectQueue
-------------------------------------------------
   Change Activity:
                   2022-03-03 10:45:
-------------------------------------------------
"""
__author__ = 'bobi'

import threading
from math import sqrt
from excel import *
import queue

from function import fun
from main import k_calculation, k_judge, distance


class clustering:
    """聚类方法类"""

    # 构造函数
    def __init__(self, dataQueue, flag, objectQueue):
        self.dataQueue = dataQueue
        self.objectQueue = objectQueue
        self.flag = flag
        # 启动线程
        threading.Thread(target=self.cluster, ).start()
        print("hello")

    # 启动聚类处理线程
    def cluster(self):
        while self.flag[0]:
            # 从队头取元素 等待时间不能错过1秒
            # print(self.dataQueue.qsize())
            if not self.dataQueue.empty():
                # pointsPeriod：一周期数据
                pointsPeriod = self.dataQueue.get(block=True, timeout=1)
                # for point in pointsPeriod[0]:
                #     print(point.angle)



            # pointsPeriod：一周期数据
            pointsPeriod = self.dataQueue.get(block=True, timeout=1)
            # for point in pointsPeriod[0]:
            #     print(point.angle)
            # todo 具体聚类方法

            # 滑动窗口大小
            window = 8

            # 聚类距离阈值   最低数量阈值
            r_max = 0.8

            num_min = 5

            # 多个目标聚类
            i = 0
            while i < pointsPeriod[0].size() - window + 1:
                prev = pointsPeriod[0][i]
                currect_point_list = [pointsPeriod[0][i]]
                for j in range(i + 1, i + window):
                    dis = fun(prev, pointsPeriod[0][j])
                    if dis <= r_max:
                        currect_point_list.append(pointsPeriod[0][j])
                        # 重置
                        prev = pointsPeriod[0][j]
                        r_max = 0.8
                    else:
                        # 跨越点阈值增加
                        r_max += 0.02
                # currect_point_list：存有一堆数据点的迭代器对象
                # if len(currect_point_list) >= num_min and k_judge(currect_point_list):
                if len(currect_point_list) >= num_min:
                    # print(currect_point_list.angle," ",currect_point_list.range)
                    czb = []
                    for t in currect_point_list:
                        czb.append((t.angle, t.range))
                    if k_judge(czb):
                        print(czb)
                    else:
                        print("斜率排除")
                    for t in range(0, len(currect_point_list)):
                        i += 1
                else:
                    print("数目排除")
                    i += 1

            # object为元组 记录当前窗口内聚类完成的object
            # object = ()
            # 存入聚类对象集中，待后续拟合使用
            # self.objectQueue.put(item=object, block=True, timeout=1)

            # todo 去除处理完的点

    # 根据初始点startPoint,动态窗口大小
    def dynamicRegulation(self, startPoint):
        windowSize = 0
        # todo 具体对应关系

        return windowSize
