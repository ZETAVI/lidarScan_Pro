import math
from math import sqrt


# 极坐标下两点距离(距离，角度)
def fun(arg1, arg2):
    return sqrt(abs(pow(arg1[0], 2) + pow(arg2[0], 2) - 2 * arg1[0] * arg2[0] * math.cos(
        math.radians(arg1[1]) - math.radians(arg2[1]))))


print(fun((1.478500009, 182.2812472), (1.463250041, 183.0468704)))
