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
import time

import src.Method.globalFunc as Fun


class clustering:
    """聚类方法类"""

    # 构造函数
    def __init__(self, dataQueue, objectQueue, showObjQueue):
        self.dataQueue = dataQueue
        self.objectQueue = objectQueue
        self.showObjQueue = showObjQueue
        # 启动线程
        threading.Thread(target=self.cluster, ).start()

    # 启动聚类处理线程
    def cluster(self):
        # 设置一个待处理链表空间
        pendingList = []
        while True:
            # 从队头取元素 等待时间不能错过1秒
            # pointsPeriod:一周期数据
            pointsPeriod = None
            if not self.dataQueue.empty():
                pointsPeriod = self.dataQueue.get(block=True, timeout=1)
            # 有可能去除失败
            if pointsPeriod is None:
                time.sleep(0.1)
                continue
            else:
                # 将取到的元组按元素点添加到待处理链表空间中
                pendingList.extend(pointsPeriod[0])

            # idx表示待聚类点的起始下标
            idx = 0
            final = []

            # 开始聚类
            while True:
                # 初始化窗口大小
                window = Fun.win_size(pendingList[idx].range)

                # 截止位置暂停
                if idx + window >= len(pendingList):
                    break

                # 初始化最少点阈值
                num_min = Fun.min_point_number(window)
                # 初始化聚类阈值
                r_max = Fun.dis_get(pendingList[idx].range)
                # 暂存聚类阈值
                t_r_max = r_max
                # 初始化跨越点阈值
                r_add = Fun.across_dis(pendingList[idx].range)

                # 初始化
                prev = pendingList[idx]
                correct_point_list = [pendingList[idx]]

                for i in range(idx + 1, idx + window - 1):
                    dis = Fun.distance(prev, pendingList[i])
                    if dis <= r_max:
                        correct_point_list.append(pendingList[i])
                        # 重置
                        prev = pendingList[i]
                        r_max = t_r_max
                    else:
                        # 跨越点阈值增加
                        r_max += r_add
                # 判断聚类对象是否符合相应的要求
                if len(correct_point_list) >= num_min:
                    if Fun.k_judge(correct_point_list):
                        final.append(correct_point_list)
                        # 聚类指针右移已聚类成功的长度
                        idx += len(correct_point_list)
                    else:
                        idx += 1
                        # print("斜率排除)
                else:
                    # print("数目排除")
                    idx += 1
            # todo 在某个地方对象会闪烁，其他地方又不会
            # self.objectQueue.put(item=final, block=True, timeout=1)
            temp = final
            self.showObjQueue.put(item=temp, block=True, timeout=1)
            # print("clustering聚类成功有:", self.showObjQueue.qsize())
            # 当一个聚类周期处理结束后  去除处理完的点(切片)
            pendingList = pendingList[idx:]
