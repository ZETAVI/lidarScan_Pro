from math import sqrt
from excel import *


# 距离计算函数


def distance(arg1, arg2):
    return sqrt(pow(arg1[0] - arg2[0], 2) + pow(arg1[1] - arg2[1], 2))


# 求斜率
def k_calculation(arg1, arg2):
    return (arg1[1] - arg2[1]) / (arg1[0] - arg2[0])


# 斜率规则判断函数
def k_judge(arg1):
    length = len(arg1)
    points = [arg1[0], arg1[int((length - 1) / 4)], arg1[int((length - 1) / 2)], arg1[int(3 * (length - 1) / 4)],
              arg1[length - 1]]
    print(points)
    if k_calculation(points[0], points[1]) < 0 and \
            k_calculation(points[1], points[2]) < 0 and \
            k_calculation(points[2], points[3]) > 0 and \
            k_calculation(points[3], points[4]) > 0:
        return True
    else:
        return False


# # (角度,距离)  异常点：(4, 2)  (11, 50)  (12, 13)  (22, 24)
# point_list = [(0, 29), (1, 28), (2, 27), (3, 26), (4, 2), (5, 21), (6, 19), (7, 19), (8, 18), (9, 15), (10, 12),
#               (11, 50), (12, 13), (13, 14), (14, 15), (15, 17), (16, 20), (17, 21), (18, 24), (19, 25), (20, 25),
#               (21, 26), (22, 29), (23, 30)]

# 获取数据
point_list = []
for i in range(2, rows + 1):
    point_list.append((table.cell(row=i, column=1).value, table.cell(row=i, column=2).value))

# 滑动窗口大小
window = 8

# 聚类阈值   最低数量阈值   初始化变量prev   聚类后列表
r_max = 0.75

num_min = window / 2 + 2

# 多个目标聚类
it = iter(range(0, len(point_list) - window + 1))
for i in it:  # 跳过的逻辑有问题
    prev = point_list[i]
    currect_point_list = [point_list[i]]
    for j in range(i + 1, i + window):
        dis = distance(prev, point_list[j])
        if dis <= r_max:
            currect_point_list.append(point_list[j])
            # 重置
            prev = point_list[j]
            # r_max = 0.7
        if len(currect_point_list) >= num_min:
            for t in range(0, window):
                try:
                    next(it)
                except StopIteration:
                    # 遇到StopIteration就退出循环
                    break
        # else:
        #     r_max = r_max + 1
    print(currect_point_list)

'''    
# 单个目标聚类
prev = point_list[0]
currect_point_list = [point_list[0]]

# 确定处理第一个点就是误差的的情况???


# 聚类
for j in range(1, len(point_list)):
    dis = distance(prev, point_list[j])
    if dis <= r_max:
        currect_point_list.append(point_list[j])
        # 重置
        prev = point_list[j]
        r_max = 5.5
    else:
        r_max = r_max + 0.5
# 是否满足最低点数
if len(currect_point_list) < num_min:
    print("点数排除")
else:
    # 判断五点斜率是否满足
    if k_judge(currect_point_list):
        print(currect_point_list)
        print('\n')
    else:
        print("斜率排除")
'''
