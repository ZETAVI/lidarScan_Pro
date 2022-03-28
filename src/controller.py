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

from src.Method import *
from src.Object import *


class controller():

    def __init__(self):
        self.flag = [True]

        # 雷达扫描数据待处理队列
        self.dataQueue = queue.Queue(maxsize=500)
        # 雷达数据显示队列
        self.showDataQueue = queue.Queue(maxsize=200)
        # 噪点过滤显示队列
        self.showFilterQueue = queue.Queue(maxsize=200)
        # 对象聚类队列
        self.objectQueue = queue.Queue(maxsize=200)
        # 对象聚类显示队列
        self.showObjQueue = queue.Queue(maxsize=200)
        # 对象2聚类显示队列
        self.showObjQueue2 = queue.Queue(maxsize=200)
        # 关键点队列
        self.keyPoints = queue.Queue(maxsize=200)
        # 活动人队列
        self.activeObjs = queue.Queue(maxsize=200)

    # todo  warning:启动线程 一个个线程打开 因为后续线程依赖前面线程的数据 所以需要前面的线程得到验证后再打开下一步线程
    def startThread(self):
        scanning(dataQueue=self.dataQueue, showDataQueue=self.showDataQueue, flag=self.flag)
        clustering(dataQueue=self.dataQueue, objectQueue=self.objectQueue, showFillterQueue=self.showFilterQueue,
                   showObjQueue=self.showObjQueue)

        # matching(objectQueue=self.objectQueue, keyPoints=self.keyPoints, showObjQueue2=self.showObjQueue2)
        MyQtWidgets(self.showDataQueue, self.showFilterQueue, self.showObjQueue).start()
        # locate_storage(keyPoints=self.keyPoints, flag=self.flag, activeObjs=self.activeObjs)
        print("进程启动成功！")

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


if __name__ == '__main__':
    # 控制台
    controller = controller()
    controller.startThread()

    # # Collect events until released
    # with keyboard.Listener(
    #         on_press=controller.on_press) as listener:
    #     # listener.setDaemon(True)
    #     listener.join()
