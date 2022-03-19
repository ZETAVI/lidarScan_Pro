# -*- codeing = utf-8 -*- 
# @Time :2022/3/17 15:01
# @Author:Meyle
# @File : matchingKeyPoint.py
# @Software: PyCharm
# @ps: 在已有的特征点序列中找相近的特征点
#
import math


def matchingKeyPoint(point, keyPoints):
    for keypoint in keyPoints:
        # 求两点距离
        distance = keypoint.position[1] ** 2 + point[1] ** 2 - 2 * keypoint.position[1] * point[1] * math.cos(
            math.radians(point[0] - keypoint.position[1]))
        # 移动距离阈值
        if distance < 0.1:
            keypoint.update(point)
            return True
    return False
