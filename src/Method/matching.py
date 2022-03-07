# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> matching
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-03 15:48
    @Desc   :拟合与特征提取
            负责计算动态窗口聚类objectQueue点集的拟合度(R_Squared)
            返回符合条件的特征点T
-------------------------------------------------
   Change Activity:
                   2022-03-03 15:48:
-------------------------------------------------
"""
__author__ = 'bobi'


class matching:
    """聚类对象拟合与特征提取"""

    def __init__(self, objectQueue):
        self.objectQueue = objectQueue
