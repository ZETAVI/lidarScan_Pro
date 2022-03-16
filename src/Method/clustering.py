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
            if not self.dataQueue.empty():
                pointsPeriod = self.dataQueue.get(block=True, timeout=1)
            # 有可能去除失败
            if pointsPeriod is None:
                continue
            else:
                # 将取到的元组按元素点添加到待处理链表空间中
                pendingList.extend(pointsPeriod[0])

            # 初始化滑动窗口大小
            window = 8

            # 聚类距离阈值   最低数量阈值
            r_max = 0.8
            num_min = 5

            # idx表示待聚类点的起始下标
            idx = 0
            final = []

            # 停止信号量
            stop = 0

            # 开始聚类
            while idx < len(pendingList):
                # 每个窗口初始化阈值
                window = Fun.win_size(pendingList[idx].range)
                num_min = Fun.min_point_number(window)
                r_max = Fun.dis_get(pendingList[idx].range)
                t = r_max
                r_add = Fun.across_dis(pendingList[idx].range)

                # 截止位置
                if idx + window >= 476:
                    stop = 1

                prev = pendingList[idx]
                correct_point_list = [pendingList[idx]]
                for j in range(idx + 1, idx + window):
                    dis = Fun.distance(prev, pendingList[j])
                    if dis <= r_max:
                        correct_point_list.append(pendingList[j])
                        # 重置
                        prev = pendingList[j]
                        r_max = t

                    else:
                        # 跨越点阈值增加
                        r_max += r_add
                if len(correct_point_list) >= num_min:
                    if Fun.k_judge(correct_point_list):
                        final.append(correct_point_list)
                    else:
                        pass
                        # print("斜率排除")
                    # 聚类指针右移已聚类成功的长度
                    idx += len(correct_point_list)
                else:
                    # print("数目排除")
                    idx += 1
                if stop == 1:
                    break
            self.objectQueue.put(item=final, block=True, timeout=1)
            # 当一个聚类周期处理结束后  去除处理完的点(切片)
            pendingList = pendingList[idx:]

    # 根据初始点startPoint,动态窗口大小
    def dynamicRegulation(self, startPoint):
        windowSize = 0
        # todo 具体对应关系

        return windowSize
