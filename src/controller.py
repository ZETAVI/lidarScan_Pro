# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> main
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-02 14:47
    @Desc   :主控制函数
            负责启动雷达扫描，运动目标识别
-------------------------------------------------
   Change Activity:
                   2022-03-02 14:47:
-------------------------------------------------
"""
__author__ = 'bobi'

import queue

from matplotlib import animation, pyplot as plt

from src.Method import *


class controller:

    def __init__(self):
        self.flag = [True]
        self.MaxL = 99999999999
        # 雷达扫描数据队列
        self.dataQueue = queue.Queue(maxsize=self.MaxL)
        # 对象聚类队列
        self.objectQueue = queue.Queue(maxsize=200)
        # 关键点队列
        self.keyPoints = queue.Queue(maxsize=200)
        # 活动人队列
        self.activeObjs = queue.Queue(maxsize=200)

    # todo  warning:启动线程 一个个线程打开 因为后续线程依赖前面线程的数据 所以需要前面的线程得到验证后再打开下一步线程
    def startThread(self):
        scanning(dataQueue=self.dataQueue, flag=self.flag)
        clustering(dataQueue=self.dataQueue, flag=self.flag, objectQueue=self.objectQueue)
        # matching(objectQueue=self.objectQueue, flag=self.flag, keyPoints=self.keyPoints)
        # locate_storage(keyPoints=self.keyPoints, flag=self.flag, activeObjs=self.activeObjs)

    # 退出监听程序
    def on_press(self, key):
        # 按下按键时执行。
        try:
            print('alphanumeric key {0} pressed , stop scanning'.format(
                key.char))
            self.flag[0] = False
        except AttributeError:
            print('special key {0} pressed '.format(
                key))

        # 通过属性判断按键类型。


# 画图函数
def animate(num):
    global color
    angle = []
    ran = []
    colors = []
    if not controller.objectQueue.empty():
        for cycle in controller.objectQueue.get(block=True, timeout=1):
            for point in cycle:
                angle.append(point.angle)
                ran.append(point.range)
                colors.append(color)
            color += 5
    else:
        time.sleep(0.5)
    lidar_polar.clear()
    lidar_polar.scatter(angle, ran, c=colors, cmap='hsv', alpha=0.95, marker='.', s=3)


if __name__ == '__main__':
    # 控制台
    controller = controller()
    controller.startThread()

    # 顏色
    color = 1
    # 初始化画布

    RMAX = 32.0
    fig = plt.figure()
    fig.canvas.set_window_title('YDLidar LIDAR Monitor')
    lidar_polar = plt.subplot(polar=True)
    lidar_polar.autoscale_view(scalex=False, scaley=False)
    lidar_polar.set_rmax(RMAX)
    lidar_polar.grid(True)
    ani = animation.FuncAnimation(fig, animate, interval=25)
    plt.show()
    plt.close()
    # print(controller.objectQueue.get(block=True, timeout=1))

    # # Collect events until released
    # with keyboard.Listener(
    #         on_press=controller.on_press) as listener:
    #     # listener.setDaemon(True)
    #     listener.join()
