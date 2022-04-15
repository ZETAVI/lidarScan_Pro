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

import numpy as np


def judege(x, y, middle_index):
    # for i in range(len(x)):
    #     print("坐标为x:", x[i], ",y:", y[i], "\n")

    tag = True  # 最终判断
    tag_left = True  # 左边判断
    tag_right = True  # 右边判断
    # 运用扫描窗口内边界点和原点的夹角角度初步排除
    # print("最低点坐标为x:", x[middle_index], ",y:", y[middle_index])
    n = len(x)

    # todo 判断直线
    if middle_index == 0 or middle_index == n - 1:
        middle = math.floor(n / 2)
        realangle = angle_calculate(x, y, 0, middle, n - 1)
        # print("大夹角为:", realangle)
        if realangle > 165:
            # print("判断结果为非人腿！\n")
            return False
    else:
        realangle = angle_calculate(x, y, 0, middle_index, n - 1)
        # print("大夹角为:", realangle)
        if realangle > 158:
            # print("判断结果为非人腿！\n")
            return False
        # if not (realangle < 145 and realangle > 92) or (realangle < 80):
        # 当大夹角在80到92度之间,还有小于50度的角判定为直角
        # if (realangle < 92 and realangle > 80) or realangle <= 50:

        # if realangle < 92 and realangle > 80:
        #     # print("判断结果为非人腿！\n")
        #     return False

        #  当大夹角在大于165度为直线
        # if realangle > 165:
        #     return False
        tag = True
        # else:
        # 进一步判断
        if n >= 5:
            realangle2 = 180
            realangle3 = 180
            if middle_index != 1:
                realangle2 = angle_calculate(x, y, 1, middle_index, n - 1)

            if middle_index != n - 2:
                realangle3 = angle_calculate(x, y, 0, middle_index, n - 2)

            if realangle2 < 165 or realangle3 < 165:
                if middle_index > 1:
                    left_realangle = angle_calculate(x, y, 0, math.floor(middle_index / 2), middle_index)
                    # print("左中间点坐标为x:", x[math.floor(middle_index / 2)], ",y:", y[math.floor(middle_index / 2)])
                    # print("左夹角为:", left_realangle)
                    if left_realangle > 170:
                        tag_left = False
                if n - 1 - middle_index > 1:
                    right_realangle = angle_calculate(x, y, middle_index, math.floor((n - 1 + middle_index) / 2), n - 1)
                    # print("右中间点坐标为x:", x[math.floor((n - 1 + middle_index) / 2)], ",y:",
                    #       y[math.floor((n - 1 + middle_index) / 2)])
                    # print("右夹角为:", right_realangle)
                    if right_realangle > 170:
                        tag_right = False
                # 当且仅当左右两边均像直线的情况下才认定为直角
                tag = tag_left or tag_right
            else:
                return False
        '''
        # 添加即时对数据进行拟合并通过拟合得到的二次函数参数进行初步排除
        z1 = np.polyfit(x, y, 2)  # 用2次多项式拟合，可改变多项式阶数；
        p1 = np.poly1d(z1)  # 得到多项式系数，按照阶数从高到低排列
        ## print(p1)  # 显示多项式
        Min = (4 * p1[0] * p1[2] - p1[1]**2) / (4 * p1[0])  #极点的y坐标 用于区分直角
        if(p1[0] > 16 or (p1[2] > 0.09) or Min > 0.0066):#此处有待修正第二个判断条件
            return tag;

        y2 = [ 9.148*x[i]**2 + 0.005358*x[i] + 0.0002134 for i in range(len(x))]
        sum = 0;
        n = len(x);
        for real_y, fit_y in zip(y, y2):
            sum = (real_y - fit_y) ^ 2 + sum;
        res = sum / n
        if(res < 2.5*10**-5):
            tag = True
        '''
        # if tag:
        #     print("判断结果为人腿！\n")
        # else:
        #     print("判断结果为非人腿！\n")
    return tag


def angle_calculate(x, y, left, middle_index, right):
    # print("左边界点：", left, "中间点：", middle_index, "右边界点：", right)
    x1 = x[left]
    y1 = y[left]
    x2 = x[middle_index]
    y2 = y[middle_index]
    x3 = x[right]
    y3 = y[right]
    # print("x1=", x1,",y1=", y1,",x2=", x2,",y2=", y2)
    c2 = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    a2 = (x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)
    b2 = (x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)
    # print("c2=", c2)

    a = math.sqrt(a2)
    b = math.sqrt(b2)
    c = math.sqrt(c2)
    # print("a=",a)
    # print("c=",c)
    pos = (a2 + c2 - b2) / (2 * a * c)  # 求出余弦值
    # print(pos)
    angle = math.acos(pos)  # 余弦值装换为弧度值
    realangle = math.degrees(angle)  # 弧度值转换为角度值

    return realangle


def transform_matching(tempObj):
    """
    将以聚类的数据点进行坐标平移与坐标转换
    angle为角度
    distance为距离
    角度和距离一一对应
    :
    """
    # 找出距离最近的点及其标号
    angle = []
    distance = []
    for point in tempObj:
        angle.append(point.angle)
        distance.append(point.range)
    middle_index = distance.index(min(distance))
    # 旋转
    Min_angle = angle[middle_index]
    t_angle = [angle[i] - Min_angle + math.pi / 2 for i in range(len(angle))]
    # 极坐标转为笛卡尔坐标
    x = [math.cos(t_angle[i]) * distance[i] for i in range(len(t_angle))]
    y = [math.sin(t_angle[i]) * distance[i] for i in range(len(t_angle))]
    # 向下平移
    y2 = [y[i] - y[middle_index] for i in range(len(y))]
    x[middle_index] = 0.0
    # 返回平移后的直角坐标和特征点在元组的序号
    return x, y2, middle_index


def transform_matching2(tempObj):
    """
    将极坐标转化为直角坐标，并返回最近点的下标
    :
    """
    # 找出距离最近的点及其标号
    angle = []
    distance = []
    for point in tempObj:
        angle.append(point.angle)
        distance.append(point.range)
    middle_index = distance.index(min(distance))
    # 极坐标转为笛卡尔坐标
    x = [math.cos(angle[i]) * distance[i] for i in range(len(angle))]
    y = [math.sin(angle[i]) * distance[i] for i in range(len(angle))]
    # 返回平移后的直角坐标和特征点在元组的序号
    return x, y, middle_index


# 极坐标下两点距离(距离，角度)
def distance(arg1, arg2):
    return sqrt(abs(pow(arg1.range, 2) + pow(arg2.range, 2) - 2 * arg1.range * arg2.range * math.cos(
        arg1.angle - arg2.angle)))


# 直角坐标下两点距离(距离，角度)
def distanceXY(arg1, arg2):
    return sqrt(pow(arg1[0] - arg2[0], 2) + pow(arg1[1] - arg2[1], 2))


# 极坐标转直角坐标
def transform_clustering(arg):
    return arg.range * math.cos(arg.angle), arg.range * math.sin(arg.angle)


# 3月30日的阈值数据
# 窗口大小获取函数（形参为第一个点距离）
def win_size(arg):
    arg = round(arg * 10)
    if arg >= 26:
        return 4
    num = [27, 27, 27, 27, 25, 20, 18, 15, 15, 14, 13, 11, 11, 9, 9, 9, 8, 8, 8, 8, 7, 7, 6, 6, 5, 5]
    return num[arg]


# # 最少点数函数 (形参为窗口大小)
def min_point_number(arg):
    # 介于1/3和1/2之间
    if 5 * arg / 12 > 3:
        return math.floor(5 * arg / 12)
    else:
        return 3


# # 聚类阈值函数（形参为第一个点距离）
def dis_get(arg):
    arg = round(arg * 10)
    if arg >= 26:
        return 0.067
    num = [0.043, 0.043, 0.043, 0.043, 0.045, 0.047, 0.050, 0.050, 0.052, 0.052, 0.0521, 0.0522, 0.0523, 0.056, 0.056,
           0.056, 0.056, 0.056, 0.057, 0.058, 0.058, 0.0582, 0.05822, 0.06, 0.06, 0.0609]
    return num[arg]


# 3月30日的阈值数据

# 极坐标两点连成线 并给定角度计算距离
def two_points_into_line(pi_1, r1, pi_2, r2, theta):
    return r1 * r2 * (np.sin(pi_2 - pi_1)) / (r1 * np.sin(theta - pi_1) - r2 * np.sin(theta - pi_2))

# # 窗口大小获取函数（形参为第一个点距离）
# def win_size(arg):
#     arg = int(arg * 10)
#     if arg >= 26:
#         return 6
#     num = [25, 25, 25, 25, 23, 18, 17, 16, 15, 14, 14, 13, 11, 11, 11, 10, 10, 9, 9, 8, 8, 8, 7, 7, 7, 7]
#     return num[arg]
#

# # 最少点数函数(形参为窗口大小)
# def min_point_number(arg):
#     if arg / 3 > 3:
#         return arg / 3
#     else:
#         return 3
#
#
# # 聚类阈值函数宽松版（形参为第一个点距离）
# def dis_get(arg):
#     arg = int(arg * 10)
#     if arg >= 26:
#         return 0.08
#     num = [0.03, 0.03, 0.03, 0.03, 0.04, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.07,
#            0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07]
#     return num[arg]
#
#
