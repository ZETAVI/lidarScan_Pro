# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> clustering
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-03 10:45
    @Desc   :聚类线程
            负责控制动态窗口与窗口点集聚类
            维护返回动态窗口聚类集合objectQueue和显示集合showObjQueue
-------------------------------------------------
   Change Activity:
                   2022-03-03 10:45:00
-------------------------------------------------
"""
__author__ = 'bobi'

import math
import time
import threading
import src.Method.globalFunc as Fun
from src.Object import keyPoint


class clustering:
    """聚类方法类"""

    # 构造函数
    def __init__(self, dataQueue, showFillterQueue, showObjQueue, keyPoints, showObjQueue2):
        self.dataQueue = dataQueue
        self.showFilterQueue = showFillterQueue
        self.showObjQueue = showObjQueue
        # 特征点集
        self.keyPoints = keyPoints
        # 结果点集
        self.showObjQueue2 = showObjQueue2
        # 启动线程
        threading.Thread(target=self.cluster, ).start()
        # 用来统计帧数变化
        self.frames = 0

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
                time.sleep(0.05)
                continue
            else:
                # 将取到的元组过滤后, 按元素点添加到待处理链表空间中
                pendingList.extend(self.filter(pointsPeriod[0]))

            # idx表示待聚类点的起始下标
            idx = 0
            final = []

            # print("!!!!新的周期开始")
            # print("不切片小范围聚类测试开始:")
            # print("本周期待处理点集共有", len(pendingList))
            # print("周期内所有点为:")
            # for point in pendingList:
            # print("角度:", point.angle, "  距离:", point.range)
            # 开始聚类
            while True:
                # print("开始聚类")
                # 初始化窗口大小
                window = Fun.win_size(pendingList[idx].range)
                # print("取起始点", idx, ",起始点的距离为", pendingList[idx].range)
                # print("窗口大小为", window)

                # 截止位置暂停
                if idx + window >= len(pendingList):
                    # print("到达周期尾部，停止聚类")
                    break

                # 初始化最少点阈值
                num_min = Fun.min_point_number(window)
                # print("初始化最少点阈值为", num_min)
                # 初始化聚类阈值
                r_max = Fun.dis_get(pendingList[idx].range)
                # print("初始化r_max阈值为", r_max)
                # 暂存聚类阈值
                t_r_max = r_max

                # 初始化
                prev = pendingList[idx]
                correct_point_list = [pendingList[idx]]

                # flag代表当前窗口聚类跨越的点次数
                flag = 0
                # print("重置flag为0")

                # print("!!!!开始遍历尝试聚类")
                for i in range(idx + 1, idx + window - 1):
                    dis = Fun.distance(prev, pendingList[i])
                    # print("prev与pendingList[", i, "]的距离:", prev.range, "===>", pendingList[i].range, "===", dis)
                    # print("x:",prev.range * math.cos(prev.angle), ",y:",prev.range * math.sin(prev.angle))
                    # print("此时r_max为", r_max)
                    if dis <= r_max:
                        correct_point_list.append(pendingList[i])
                        # print("该点", i, "符合距离阈值,加入聚类集合")
                        # 重置
                        prev = pendingList[i]
                        r_max = t_r_max
                        # print("此时重置r_max为", r_max)
                    else:
                        # 跨越点阈值增加  跨越点次数增加
                        r_max += 0.75 * t_r_max
                        flag += 1
                        if flag > 2:
                            idx += 1
                            # print("跨越点过多，取消本次聚类")
                            # print("更新idx开始准备下一轮尝试,idx更新为", idx)
                            break
                        # print("dis > r_max , 出现较远点,扩大r_max，此时r_max为", r_max)
                # print("!!!!尝试聚类结束,聚类成功点集长度为", len(correct_point_list), "  num_min下限为", num_min)
                # 判断聚类对象是否符合相应的要求
                # print("开始判断聚类对象是否符合要求")
                if len(correct_point_list) >= num_min:
                    if self.judge(correct_point_list):
                        # print("聚类成功")
                        final.append(correct_point_list)
                        # 聚类指针右移已聚类成功的长度
                        idx += len(correct_point_list)
                    else:
                        idx += 1
                        # print("凹凸排除")
                else:
                    # print("数目排除")
                    idx += 1
                # print("更新idx开始准备下一轮尝试,idx更新为", idx)

            # print("本周期聚类目标共有", len(final))
            self.showObjQueue.put(item=final, block=True, timeout=1)

            # matching转移代码:用于排除不合适的聚类目标
            objectShow = []
            for tempObj in final:
                x, y, middle_index = Fun.transform_matching2(tempObj)
                if Fun.judege(x, y, middle_index):
                    # 判断上一帧的特征点中是否有相近特征点 有的话就当场替换，没有就添加
                    # if matchingKeyPoint(tempObj[middle_index], self.keyPoints):
                    #     continue
                    # 如果初步符合特征,提取特征点
                    tempkeypoint = keyPoint(position=tempObj[middle_index], frames=self.frames)

                    # print("找到符合的特征点")
                    # print(tempObj[middle_index].angle, tempObj[middle_index].range)

                    # 将聚类对象添加入待显示对象队列
                    objectShow.append(tempObj)

                    # 存入keyPoints队列等待后续处理
                    self.keyPoints.put(item=tempkeypoint, block=True, timeout=1)
                    # print(tempkeypoint)

            # todo 第三步 将当前符合条件的所有聚类目标进行显示
            self.showObjQueue2.put(item=objectShow, block=True, timeout=1)
            # print("clustering聚类成功有:", self.showObjQueue.qsize())
            self.frames = (self.frames + 1) % 9999999
            print(time.time())
            # 当一个聚类周期处理结束后  去除处理完
            pendingList = pendingList[idx:]

    # 杂点过滤函数
    def filter(self, pointsPeriod):
        points = []
        ans = []
        # print(len(pointsPeriod))
        for point in pointsPeriod:
            if 0.04 < point.range < 2.6:
                points.append(point)

        length = len(points)
        # print(length)
        for i in range(0, length - 1):
            prev = points[i - 1]
            cur = points[i]
            nxt = points[i + 1]
            if Fun.distance(prev, cur) < 0.15 or Fun.distance(cur, nxt) < 0.15:
                ans.append(cur)

        # 最后一个点
        cur = points[length - 1]
        prev = points[length - 2]
        nxt = points[0]
        if Fun.distance(cur, prev) < 0.15 or Fun.distance(cur, nxt) < 0.15:
            ans.append(cur)

        self.showFilterQueue.put(item=ans, block=True, timeout=1)
        return ans

    # 凹凸检测函数
    def judge(self, points):
        ran = 1000
        idx = 1000
        length = len(points)
        count = 0
        pi_1 = points[0].angle
        r1 = points[0].range
        pi_2 = points[length - 1].angle
        r2 = points[length - 1].range

        if pi_1 > pi_2:
            temp = pi_1
            pi_1 = pi_2
            pi_2 = temp
            temp = r1
            r1 = r2
            r2 = temp

        for i in range(0, length):
            disToLine = Fun.two_points_into_line(pi_1, r1, pi_2, r2, points[i].angle)
            if disToLine < points[i].range:
                count += 1

            if ran >= points[i].range:
                ran = points[i].range
                idx = i

        if count >= length * 3 / 4:
            # print("超过两点直线的点数过多 ", count, "个大于等于", length, "的一半, 排除")
            return False
        else:
            return True
        # # print("凹凸检测函数取最低点i：", idx)
        # if idx == 0 or idx == length - 1:
        #     # print("最低点为端点，排除")
        #     return False
        # else:
        #     # print("最低点非端点，通过")
        #     return True
