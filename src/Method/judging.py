# -*- codeing = utf-8 -*- 
# @Time :2022/3/4 15:53 
# @Author:Meyle
# @File : judging.py 
# @Software: PyCharm
# @ps: 将扫描数据与腿部模型函数进行比较，根据它们的标准差判断是否为类人腿物体
#       函数：9.148*x.^2 + 0.005358*x + 0.0002134;
#       阈值：2.5E-5
def transform(x, y):

    tag = False
    y2 = [ 9.148*x[i]**2 + 0.005358*x[i] + 0.0002134 for i in range(len(x))]
    sum = 0;
    n = len(x);
    for real_y, fit_y in zip(y, y2):
        sum = (real_y - fit_y) ^ 2 + sum;
    res = sum / n
    if(res < 2.5*10**-5):
        tag = True
    return tag

