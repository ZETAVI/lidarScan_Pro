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

import src.Method.globalFunc as Fun


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
        # pointsPeriod：一周期数据
        pointsPeriod = None

        # 设置一个待处理链表空间
        pendingList = []

        while self.flag[0]:
            # 从队头取元素 等待时间不能错过1秒
            # print(self.dataQueue.qsize())
            if not self.dataQueue.empty():
                pointsPeriod = self.dataQueue.get(block=True, timeout=1)
                # for point in pointsPeriod[0]:
                #     print(point.angle)

            # 有可能去除失败
            if pointsPeriod is None:
                continue
            else:
                # 将取到的元组按元素点添加到待处理链表空间中
                pendingList.extend(pointsPeriod[0])
            # todo 具体聚类方法

            # 滑动窗口大小
            window = 8

            # 聚类距离阈值   最低数量阈值
            # todo
            r_max = 0.8

            num_min = 5

            # 多个目标聚类
            # idx表示待聚类点的起始下标
            idx = 0
            czb = []
            while idx < len(pendingList) - window + 1:
                prev = pointsPeriod[0][idx]
                correct_point_list = [pointsPeriod[0][idx]]
                for j in range(idx + 1, idx + window):
                    dis = Fun.distance(prev, pointsPeriod[0][j])
                    if dis <= r_max:
                        correct_point_list.append(pointsPeriod[0][j])
                        # 重置
                        prev = pointsPeriod[0][j]
                        r_max = 0.8
                    else:
                        # 跨越点阈值增加
                        r_max += 0.02
                # correct_point_list：存有一堆数据点的迭代器对象
                # if len(correct_point_list) >= num_min and k_judge(correct_point_list):
                if len(correct_point_list) >= num_min:
                    # print(correct_point_list.angle," ",correct_point_list.range)
                    if Fun.k_judge(correct_point_list):
                        # print(czb)
                        czb.append(correct_point_list)
                    else:
                        pass
                        # print("斜率排除")
                    # 聚类指针右移已聚类成功的长度
                    idx += len(correct_point_list)
                else:
                    print("数目排除")
                    idx += 1

            # object为元组 记录当前窗口内聚类完成的object
            # object = ()
            # 存入聚类对象集中，待后续拟合使用
            # self.objectQueue.put(item=object, block=True, timeout=1)

            # todo 当一个聚类周期处理结束后  去除处理完的点(切片)
            pendingList = pendingList[idx:]

    # 根据初始点startPoint,动态窗口大小
    def dynamicRegulation(self, startPoint):
        windowSize = 0
        # todo 具体对应关系

        return windowSize
