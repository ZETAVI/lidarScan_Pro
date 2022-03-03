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
import queue


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
                pointsPeriod = self.dataQueue.get(block=True, timeout=1)
                # for point in pointsPeriod[0]:
                #     print(point.angle)

            # todo 具体聚类方法
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
