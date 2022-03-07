# -*- codeing = utf-8 -*-
# @Time :2022/3/3 21:17
# @Author:Meryle
# @File : transfor.py
# @Software: PyCharm
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> scanning
    @IDE    :PyCharm
    @Author :Meryle
    @Date   :2022-03-02 16:02
    @Desc   :扫描单元
            将雷达数据
-------------------------------------------------
   Change Activity:
                   2022-03-02 16:02:
-------------------------------------------------
"""
import random
import matplotlib.pyplot as plt

# #################################拟合优度R^2的计算######################################
import numpy as np


def __sst(y_no_fitting):
    """
    计算SST(total sum of squares) 总平方和
    :param y_no_predicted: List[int] or array[int] 待拟合的y
    :return: 总平方和SST
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_no_fitting]
    sst = sum(s_list)
    return sst


def __ssr(y_fitting, y_no_fitting):
    """
    计算SSR(regression sum of squares) 回归平方和
    :param y_fitting: List[int] or array[int]  拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 回归平方和SSR
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_fitting]
    ssr = sum(s_list)
    return ssr


def __sse(y_fitting, y_no_fitting):
    """
    计算SSE(error sum of squares) 残差平方和
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 残差平方和SSE
    """
    s_list = [(y_fitting[i] - y_no_fitting[i])**2 for i in range(len(y_fitting))]
    sse = sum(s_list)
    return sse


def goodness_of_fit(y_fitting, y_no_fitting):
    """
    计算拟合优度R^2
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 拟合优度R^2
    """
    SSR = __ssr(y_fitting, y_no_fitting)
    SST = __sst(y_no_fitting)
    SSE = __sse(y_fitting, y_no_fitting)
    rr = 1- SSE /SST
    return rr

# 生成待拟合数据
#a = np.arange(10)
x = [#0.071 ,0.059 ,0.046 ,0.035 ,0.023 ,0.012 ,0.000 ,-0.011 ,-0.022 ,-0.034 ]
    0.0404254 ,0.0316393 ,0.0233339 ,0.0153201 ,0.0076345 ,0.0000000 ,-0.0076607 ,-0.0152123 ,-0.0231731 ,-0.0308868 ,-0.0386721 ,-0.0466908 ,-0.0546335 ,-0.0633099 ]
y = [#0.025,0.018 ,0.012 ,0.005 ,0.002 ,0.006 ,0.000 ,0.009 ,0.025 ,0.049]
    0.0208990,0.0111586, 0.0065386, 0.0017995, -0.0000500, 0.0000000, 0.0019499, 0.0038029, 0.0065450, 0.0091954, 0.0117446, 0.0141783, 0.0185251, 0.0287340 ]
# 通过添加正态噪声，创造拟合好的数据
#b = a + 0.4 * np.random.normal(size=len(a))
y2 = [7.964*(x[i]**2) + 0.07553*x[i] + 0.00146 for i in range(len(x))]
y4 = [round(i,6)for i in y2]
print("原始数据为: ", y)
print("拟合数据为: ", y2)
print("舍弃一部分小数为: ", y4)
rr = goodness_of_fit(y4, y)
print("拟合优度为:", rr)
"""
plt.plot(a, a, color="#72CD28", label='原始数据')
plt.plot(a, b, color="#EBBD43", label='拟合数据')
plt.legend()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.show()
"""