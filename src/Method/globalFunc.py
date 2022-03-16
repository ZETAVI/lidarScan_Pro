# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> clustering
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-03 10:45
    @Desc   :通用方法

-------------------------------------------------
   Change Activity:
                   2022-03-03 10:45:
-------------------------------------------------
"""
__author__ = 'bobi'

import math
from math import sqrt


# 极坐标下两点距离(距离，角度)
def distance(arg1, arg2):
    return sqrt(abs(pow(arg1.range, 2) + pow(arg2.range, 2) - 2 * arg1.range * arg2.range * math.cos(
        math.radians(arg1.angle) - math.radians(arg2.angle))))


# 极坐标转直角坐标
def transform(arg):
    return arg.range * math.cos(arg.angle), arg.range * math.sin(arg.angle)


# 求斜率
def k_calculation(arg1, arg2):
    if arg1[0] - arg2[0] == 0:
        return 0
    else:
        return (arg1[1] - arg2[1]) / (arg1[0] - arg2[0])


# 斜率规则判断函数
def k_judge(arg1):
    length = len(arg1)
    points = [arg1[0], arg1[int((length - 1) / 4)], arg1[int((length - 1) / 2)], arg1[int(3 * (length - 1) / 4)],
              arg1[length - 1]]
    if k_calculation(transform(points[0]), transform(points[2])) < 0 and \
            k_calculation(transform(points[2]), transform(points[4])) > 0:
        return True
    else:
        return False


# 窗口大小获取函数（形参为第一个点距离）
def win_size(arg):
    arg = arg * 100
    if arg >= 250:
        return 5
    elif arg >= 240:
        return 5
    elif arg >= 230:
        return 5
    elif arg >= 220:
        return 6
    elif arg >= 210:
        return 6
    elif arg >= 200:
        return 6
    elif arg >= 190:
        return 7
    elif arg >= 180:
        return 7
    elif arg >= 170:
        return 7
    elif arg >= 160:
        return 8
    elif arg >= 150:
        return 8
    elif arg >= 140:
        return 8
    elif arg >= 130:
        return 9
    elif arg >= 120:
        return 9
    elif arg >= 110:
        return 11
    elif arg >= 100:
        return 12
    elif arg >= 90:
        return 12
    elif arg >= 80:
        return 12
    elif arg >= 70:
        return 14
    elif arg >= 60:
        return 14
    elif arg >= 50:
        return 16
    elif arg >= 40:
        return 21
    else:
        return 25


# 最少点数函数(形参为窗口大小)
def min_point_number(arg):
    if arg / 2 > 3:
        return arg / 2
    else:
        return 3


# 聚类阈值函数（形参为第一个点距离）
def dis_get(arg):
    arg = arg * 100
    if 180 <= arg < 260:
        return 0.055
    elif 170 <= arg < 180:
        return 0.051
    elif 160 <= arg < 170:
        return 0.049
    elif 120 <= arg < 160:
        return 0.045
    elif 110 <= arg < 120:
        return 0.039
    elif 100 <= arg < 110:
        return 0.037
    elif 50 <= arg < 100:
        return 0.034
    elif 40 <= arg < 50:
        return 0.025
    else:
        return 0.02


# 跨越点阈值函数（形参为第一个点距离）
def across_dis(arg):
    arg = arg * 100
    if arg >= 250:
        return 0.042
    elif arg >= 240:
        return 0.037
    elif arg >= 230:
        return 0.037
    elif arg >= 220:
        return 0.035
    elif arg >= 210:
        return 0.035
    elif arg >= 200:
        return 0.034
    elif arg >= 190:
        return 0.032
    elif arg >= 180:
        return 0.032
    elif arg >= 170:
        return 0.032
    elif arg >= 160:
        return 0.029
    elif arg >= 150:
        return 0.029
    elif arg >= 140:
        return 0.027
    elif arg >= 130:
        return 0.025
    elif arg >= 120:
        return 0.024
    elif arg >= 110:
        return 0.022
    elif arg >= 100:
        return 0.021
    elif arg >= 90:
        return 0.018
    elif arg >= 80:
        return 0.017
    elif arg >= 70:
        return 0.015
    elif arg >= 60:
        return 0.014
    elif arg >= 50:
        return 0.014
    elif arg >= 40:
        return 0.010
    else:
        return 0.005
