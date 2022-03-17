# -*- codeing = utf-8 -*- 
# @Time :2022/3/4 15:53 
# @Author:Meyle
# @File : judging.py 
# @Software: PyCharm
# @ps: 将扫描数据与腿部模型函数进行比较，根据它们的标准差判断是否为类人腿物体
#       函数：9.148*x.^2 + 0.005358*x + 0.0002134
#       阈值：2.5E-5
#
#  @Time :2022/3/6 11:30 修改
#  或即时将数据进行二项式拟合比较a,b,c参数来提高准确度    各个参数的阈值仍有改良或确认余地
import math

import numpy as np


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
    # print(p1)  # 显示多项式
    Min = (4 * p1[0] * p1[2] - p1[1] ** 2) / (4 * p1[0])  # 极点的y坐标 用于区分直角
    if p1[0] > 16 or (p1[2] > 0.09) or Min > 0.0066:  # 此处有待修正第二个判断条件
        return tag

    y2 = [9.148 * x[i] ** 2 + 0.005358 * x[i] + 0.0002134 for i in range(len(x))]
    sum = 0

    for real_y, fit_y in zip(y, y2):
        sum = (real_y - fit_y) ^ 2 + sum
    res = sum / n
    if res < 2.5 * 10 ** -5:
        tag = True
    '''
    return tag
