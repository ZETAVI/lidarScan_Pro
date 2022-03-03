# -*- codeing = utf-8 -*- 
# @Time :2022/3/3 21:17 
# @Author:Eric 
# @File : transfor.py 
# @Software: PyCharm
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> scanning
    @IDE    :PyCharm
    @Author :Meryle
    @Date   :2022-03-02 16:02
    @Desc   :扫描单元
            获取雷达扫描仪的数据，添加到队列中
-------------------------------------------------
   Change Activity:
                   2022-03-02 16:02:
-------------------------------------------------
"""
import math
def transform(angle, distance):
    """
    将以聚类的数据点进行坐标平移与坐标转换
    angle为角度
    distance为距离
    角度和距离一一队以ing
    :
    """
    #距离最近的点的标号
    middle_index = distance.index(min(distance))
    #旋转
    t_angle = [angle[i] - angle[middle_index] + 90 for i in range(len(angle))]
    #极坐标转为笛卡尔坐标
    x = [math.cos(math.radians(t_angle[i])) * distance[i] for i in range(len(t_angle))]
    y = [math.sin(math.radians(t_angle[i])) * distance[i] for i in range(len(t_angle))]
    #向下平移
    y2 = [y[i] - y[middle_index] for i in range(len(y))]

    return (x,y2)