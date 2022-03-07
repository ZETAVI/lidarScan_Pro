import math
from math import sqrt


# 极坐标下两点距离(距离，角度)
def fun(arg1, arg2):
    return sqrt(abs(pow(arg1.range, 2) + pow(arg2.range, 2) - 2 * arg1.range * arg2.range * math.cos(
        math.radians(arg1.angle) - math.radians(arg2.angle))))


# 极坐标点转直角坐标点
def polar_coordinatesTorectangular_coordinates(arg):
    return []


# 距离计算函数
def distance(arg1, arg2):
    return sqrt(pow(arg1[0] - arg2[0], 2) + pow(arg1[1] - arg2[1], 2))


# 极坐标转直角坐标
def transform(arg):
    return arg[1] * math.cos(arg[0]), arg[1] * math.sin(arg[0])


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
