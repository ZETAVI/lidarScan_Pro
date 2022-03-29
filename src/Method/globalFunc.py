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


def judege(x, y, middle_index):
    for i in range(len(x)):
        print("坐标为x:", x[i], ",y:", y[i], "\n")

    tag = False  # 最终判断
    tag_left = True  # 左边判断
    tag_right = True  # 右边判断
    # 运用扫描窗口内边界点和原点的夹角角度初步排除
    print("最低点坐标为x:", x[middle_index], ",y:", y[middle_index])
    n = len(x)
    # todo 判断直线
    if middle_index == 0 or middle_index == n - 1:
        middle = math.floor(n / 2)
        realangle = angle_calculate(x, y, 0, middle, n - 1)
        if realangle > 155:
            print("大夹角为:", realangle)
            print("判断结果为非人腿！\n")
            return False
    else:
        realangle = angle_calculate(x, y, 0, middle_index, n - 1)
        print("大夹角为:", realangle)
        if realangle > 155:
            print("判断结果为非人腿！\n")
            return False
        # if not (realangle < 145 and realangle > 92) or (realangle < 80):
        # 当大夹角在80到92度之间,还有小于50度的角判定为直角
        # if (realangle < 92 and realangle > 80) or realangle <= 50:

        # if realangle < 92 and realangle > 80:
        #     print("判断结果为非人腿！\n")
        #     return False

        #  当大夹角在大于165度为直线
        # if realangle > 165:
        #     return False
        tag = True
        # else:
        # 进一步判断
        if n >= 5:
            if middle_index != 1:
                realangle2 = angle_calculate(x, y, 1, middle_index, n - 1)
            else:
                realangle2 = angle_calculate(x, y, 1, math.floor((n - 2) / 2), n - 1)
            if middle_index != n - 2:
                realangle3 = angle_calculate(x, y, 0, middle_index, n - 2)
            else:
                realangle3 = angle_calculate(x, y, 0, math.floor((n - 2) / 2), n - 2)
            if realangle2 > 170 or realangle3 > 170:
                return False;
            if middle_index > 1:
                left_realangle = angle_calculate(x, y, 0, math.floor(middle_index / 2), middle_index)
                print("左中间点坐标为x:", x[math.floor(middle_index / 2)], ",y:", y[math.floor(middle_index / 2)])
                print("左夹角为:", left_realangle)
                if left_realangle > 170:
                    tag_left = False
            if n - 1 - middle_index > 1:
                right_realangle = angle_calculate(x, y, middle_index, math.floor((n - 1 + middle_index) / 2), n - 1)
                print("右中间点坐标为x:", x[math.floor((n - 1 + middle_index) / 2)], ",y:",
                      y[math.floor((n - 1 + middle_index) / 2)])
                print("右夹角为:", right_realangle)
                if right_realangle > 170:
                    tag_right = False
            # 当且仅当左右两边均像直线的情况下才认定为直角
            tag = tag_left or tag_right
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
        if tag:
            print("判断结果为人腿！\n")
        else:
            print("判断结果为非人腿！\n")
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
    arg = int(arg * 10)
    if arg >= 26:
        return 6
    num = [25, 25, 25, 25, 23, 18, 17, 16, 15, 14, 14, 13, 11, 11, 11, 10, 10, 9, 9, 8, 8, 8, 7, 7, 7, 7]
    return num[arg]

    # arg = arg * 100
    # if arg >= 250:
    #     return 7
    # elif arg >= 240:
    #     return 7
    # elif arg >= 230:
    #     return 7
    # elif arg >= 220:
    #     return 7
    # elif arg >= 210:
    #     return 8
    # elif arg >= 200:
    #     return 8
    # elif arg >= 190:
    #     return 8
    # elif arg >= 180:
    #     return 9
    # elif arg >= 170:
    #     return 9
    # elif arg >= 160:
    #     return 10
    # elif arg >= 150:
    #     return 10
    # elif arg >= 140:
    #     return 11
    # elif arg >= 130:
    #     return 11
    # elif arg >= 120:
    #     return 11
    # elif arg >= 110:
    #     return 13
    # elif arg >= 100:
    #     return 14
    # elif arg >= 90:
    #     return 14
    # elif arg >= 80:
    #     return 15
    # elif arg >= 70:
    #     return 16
    # elif arg >= 60:
    #     return 17
    # elif arg >= 50:
    #     return 18
    # elif arg >= 40:
    #     return 23
    # else:
    #     return 25


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
    arg = int(arg * 10)
    if arg >= 26:
        return 0.08
    num = [0.03, 0.03, 0.03, 0.03, 0.04, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.06, 0.06, 0.07,
           0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07]
    return num[arg]

    # arg = arg * 100
    # if 180 <= arg < 260:
    #     return 0.07
    # elif 170 <= arg < 180:
    #     return 0.07
    # elif 160 <= arg < 170:
    #     return 0.06
    # elif 120 <= arg < 160:
    #     return 0.06
    # elif 110 <= arg < 120:
    #     return 0.05
    # elif 100 <= arg < 110:
    #     return 0.05
    # elif 50 <= arg < 100:
    #     return 0.05
    # elif 40 <= arg < 50:
    #     return 0.04
    # else:
    #     return 0.03


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
