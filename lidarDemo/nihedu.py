
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
x = [0.0708 ,0.0586 ,0.0464 ,0.0345 ,0.0230 ,0.0117 ,0.0000 ,-0.0112 ,-0.0224 ,-0.0344 ]
    #0.0404254 ,0.0316393 ,0.0233339 ,0.0153201 ,0.0076345 ,0.0000000 ,-0.0076607 ,-0.0152123 ,-0.0231731 ,-0.0308868 ,-0.0386721 ,-0.0466908 ,-0.0546335 ,-0.0633099 ]
y = [0.0254,0.0180 ,0.0118 ,0.0053 ,0.0017 ,0.0060 ,0.0000 ,0.0089 ,0.0247 ,0.0493]
    #0.0208990,0.0111586, 0.0065386, 0.0017995, -0.0000500, 0.0000000, 0.0019499, 0.0038029, 0.0065450, 0.0091954, 0.0117446, 0.0141783, 0.0185251, 0.0287340 ]
# 通过添加正态噪声，创造拟合好的数据
#b = a + 0.4 * np.random.normal(size=len(a))
y2 = [7.964*(x[i]**2) + 0.07553*x[i] + 0.00146 for i in range(len(x))]
print("原始数据为: ", y)
print("拟合数据为: ", y2)

rr = goodness_of_fit(y2, y)
print("拟合优度为:", rr)
"""
plt.plot(a, a, color="#72CD28", label='原始数据')
plt.plot(a, b, color="#EBBD43", label='拟合数据')
plt.legend()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.show()
"""