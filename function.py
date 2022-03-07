import math
from math import sqrt


# 极坐标下两点距离(距离，角度)
def fun(arg1, arg2):
    return sqrt(abs(pow(arg1.range, 2) + pow(arg2.range, 2) - 2 * arg1.range * arg2.range * math.cos(
        math.radians(arg1.angle) - math.radians(arg2.angle))))

# 极坐标点转直角坐标点
def polar_coordinatesTorectangular_coordinates(arg):
    return []

