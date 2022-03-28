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


def judege(x, y):
    tag = False
    # 运用扫描窗口内边界点和原点的夹角角度初步排除
    n = len(x)
    if x[0] != 0 and x[n - 1] != 0:
        x1 = x[0]
        y1 = y[0]
        x2 = 0
        y2 = 0
        x3 = x[n - 1]
        y3 = y[n - 1]
        a2 = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        b2 = (x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2)
        c2 = (x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)
        a = math.sqrt(a2)
        b = math.sqrt(b2)
        c = math.sqrt(c2)
        pos = (a2 + b2 - c2) / (2 * a * b)  # 求出余弦值
        angle = math.acos(pos)  # 余弦值装换为弧度值
        realangle = math.degrees(angle)  # 弧度值转换为角度值
        if realangle < 145 or realangle > 95:
            tag = True

    '''
    # 添加即时对数据进行拟合并通过拟合得到的二次函数参数进行初步排除
    z1 = np.polyfit(x, y, 2)  # 用2次多项式拟合，可改变多项式阶数；
    p1 = np.poly1d(z1)  # 得到多项式系数，按照阶数从高到低排列
    #print(p1)  # 显示多项式
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
    return tag


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
    # for point in tempObj:
    #     point[0] = point[0] - tempObj[index][0] + 90

    t_angle = [angle[i] - Min_angle + 90 for i in range(len(angle))]
    # 极坐标转为笛卡尔坐标

    x = [math.cos(math.radians(t_angle[i])) * distance[i] for i in range(len(t_angle))]
    y = [math.sin(math.radians(t_angle[i])) * distance[i] for i in range(len(t_angle))]
    # 向下平移
    y2 = [y[i] - y[middle_index] for i in range(len(y))]
    # 返回平移后的直角坐标和特征点在元组的序号
    return x, y2, middle_index


# 极坐标下两点距离(距离，角度)
def distance(arg1, arg2):
    return sqrt(abs(pow(arg1.range, 2) + pow(arg2.range, 2) - 2 * arg1.range * arg2.range * math.cos(
        arg1.angle - arg2.angle)))


# 极坐标转直角坐标
def transform_clustering(arg):
    return arg.range * math.cos(arg.angle), arg.range * math.sin(arg.angle)


# 求斜率
def k_calculation(arg1, arg2):
    print("点的坐标", arg1[0], arg1[1], arg2[0], arg2[1])
    if arg1[0] - arg2[0] == 0:
        return 0
    else:
        k = (arg1[1] - arg2[1]) / (arg1[0] - arg2[0])
        print("两点斜率为", k)
        return k


# 斜率规则判断函数
def k_judge(arg1):
    length = len(arg1)
    points = [arg1[0], arg1[int((length - 1) / 4)], arg1[int((length - 1) / 2)], arg1[int(3 * (length - 1) / 4)],
              arg1[length - 1]]
    print("选取的三个点为")
    if k_calculation(transform_clustering(points[0]), transform_clustering(points[2])) < 0 and \
            k_calculation(transform_clustering(points[2]), transform_clustering(points[4])) > 0:
        return True
    else:
        return False


# 窗口大小获取函数（形参为第一个点距离）
def win_size(arg):
    arg = arg * 100
    if arg >= 250:
        return 7
    elif arg >= 240:
        return 7
    elif arg >= 230:
        return 7
    elif arg >= 220:
        return 7
    elif arg >= 210:
        return 8
    elif arg >= 200:
        return 8
    elif arg >= 190:
        return 8
    elif arg >= 180:
        return 9
    elif arg >= 170:
        return 9
    elif arg >= 160:
        return 10
    elif arg >= 150:
        return 10
    elif arg >= 140:
        return 11
    elif arg >= 130:
        return 11
    elif arg >= 120:
        return 11
    elif arg >= 110:
        return 13
    elif arg >= 100:
        return 14
    elif arg >= 90:
        return 14
    elif arg >= 80:
        return 15
    elif arg >= 70:
        return 16
    elif arg >= 60:
        return 17
    elif arg >= 50:
        return 18
    elif arg >= 40:
        return 23
    else:
        return 25


# 最少点数函数(形参为窗口大小)
def min_point_number(arg):
    if arg / 3 > 3:
        return arg / 3
    else:
        return 3


# # 聚类阈值函数严格版（形参为第一个点距离）
# def dis_get(arg):
#     arg = arg * 100
#     if 180 <= arg < 260:
#         return 0.055
#     elif 170 <= arg < 180:
#         return 0.051
#     elif 160 <= arg < 170:
#         return 0.049
#     elif 120 <= arg < 160:
#         return 0.045
#     elif 110 <= arg < 120:
#         return 0.039
#     elif 100 <= arg < 110:
#         return 0.037
#     elif 50 <= arg < 100:
#         return 0.034
#     elif 40 <= arg < 50:
#         return 0.025
#     else:
#         return 0.02

# 聚类阈值函数宽松版（形参为第一个点距离）
def dis_get(arg):
    arg = arg * 100
    if 180 <= arg < 260:
        return 0.07
    elif 170 <= arg < 180:
        return 0.07
    elif 160 <= arg < 170:
        return 0.06
    elif 120 <= arg < 160:
        return 0.06
    elif 110 <= arg < 120:
        return 0.05
    elif 100 <= arg < 110:
        return 0.05
    elif 50 <= arg < 100:
        return 0.05
    elif 40 <= arg < 50:
        return 0.04
    else:
        return 0.03


# # 跨越点阈值函数严格版（形参为第一个点距离）
# def across_dis(arg):
#     arg = arg * 100
#     if arg >= 250:
#         return 0.042
#     elif arg >= 240:
#         return 0.037
#     elif arg >= 230:
#         return 0.037
#     elif arg >= 220:
#         return 0.035
#     elif arg >= 210:
#         return 0.035
#     elif arg >= 200:
#         return 0.034
#     elif arg >= 190:
#         return 0.032
#     elif arg >= 180:
#         return 0.032
#     elif arg >= 170:
#         return 0.032
#     elif arg >= 160:
#         return 0.029
#     elif arg >= 150:
#         return 0.029
#     elif arg >= 140:
#         return 0.027
#     elif arg >= 130:
#         return 0.025
#     elif arg >= 120:
#         return 0.024
#     elif arg >= 110:
#         return 0.022
#     elif arg >= 100:
#         return 0.021
#     elif arg >= 90:
#         return 0.018
#     elif arg >= 80:
#         return 0.017
#     elif arg >= 70:
#         return 0.015
#     elif arg >= 60:
#         return 0.014
#     elif arg >= 50:
#         return 0.014
#     elif arg >= 40:
#         return 0.010
#     else:
#         return 0.005

# 跨越点阈值函数宽松版（形参为第一个点距离）
def across_dis(arg):
    arg = arg * 100
    if arg >= 250:
        return 0.06
    elif arg >= 240:
        return 0.05
    elif arg >= 230:
        return 0.05
    elif arg >= 220:
        return 0.05
    elif arg >= 210:
        return 0.05
    elif arg >= 200:
        return 0.05
    elif arg >= 190:
        return 0.05
    elif arg >= 180:
        return 0.05
    elif arg >= 170:
        return 0.05
    elif arg >= 160:
        return 0.04
    elif arg >= 150:
        return 0.04
    elif arg >= 140:
        return 0.04
    elif arg >= 130:
        return 0.04
    elif arg >= 120:
        return 0.04
    elif arg >= 110:
        return 0.04
    elif arg >= 100:
        return 0.04
    elif arg >= 90:
        return 0.03
    elif arg >= 80:
        return 0.03
    elif arg >= 70:
        return 0.03
    elif arg >= 60:
        return 0.03
    elif arg >= 50:
        return 0.03
    elif arg >= 40:
        return 0.02
    else:
        return 0.02
