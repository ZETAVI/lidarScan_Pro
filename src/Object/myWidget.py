# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> main
    @IDE    :PyCharm
    @Author :Mr. CAI
    @Date   :2022-03-02 14:47
    @Desc   :绘图类
            负责显示结果
-------------------------------------------------
   Change Activity:C
                   2022-03-16 16:46:
-------------------------------------------------
"""
__author__ = 'bobi'

import threading
import time

import numpy as np
from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
from src.Method.globalFunc import *


class MyWidget(pg.GraphicsWindow):

    def __init__(self, data, parent=None):
        super().__init__(parent=parent)
        self.data = data
        # 画图初始化
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        # 雷达数据原图
        self.timer1 = QtCore.QTimer(self)
        self.timer1.setInterval(10)  # in milliseconds
        self.timer1.start()
        self.timer1.timeout.connect(self.onNewData1)
        self.plotItem1 = self.addPlot(title="Lidar points")
        self.plotDataItem1 = self.plotItem1.plot([], pen=None, symbolBrush=(255, 0, 0), symbolSize=5, symbolPen=None)

        # 雷达聚类图
        self.timer2 = QtCore.QTimer(self)
        self.timer2.setInterval(10)  # in milliseconds
        self.timer2.start()
        self.timer2.timeout.connect(self.onNewData2)
        self.plotItem2 = self.addPlot(title="Lidar2 points")
        self.plotDataItem2 = self.plotItem2.plot([], pen=None, symbolBrush=(255, 0, 0),
                                                 symbolSize=5, symbolPen=None)

        self.nextRow()

        self.timer3 = QtCore.QTimer(self)
        self.timer3.setInterval(10)  # in milliseconds
        self.timer3.start()
        self.timer3.timeout.connect(self.onNewData3)
        self.plotItem3 = self.addPlot(title="Lidar3 points")
        self.plotDataItem3 = self.plotItem3.plot([], pen=None, symbolBrush=(255, 0, 0),
                                                 symbolSize=5, symbolPen=None)

        # 雷达聚类处理图
        self.timer4 = QtCore.QTimer(self)
        self.timer4.setInterval(10)  # in milliseconds
        self.timer4.start()
        self.timer4.timeout.connect(self.onNewData4)
        self.plotItem4 = self.addPlot(title="Lidar4 points")
        self.plotDataItem4 = self.plotItem4.plot([], pen=None, symbolBrush=(255, 0, 0), symbolSize=5, symbolPen=None)

    def onNewData1(self):
        data = self.data[0]
        # print("showDataQueue size:", data.qsize())
        if data.qsize() > 30:
            self.timer1.setInterval(5)
        elif data.qsize() < 25:
            self.timer1.setInterval(130)
        if not data.empty():
            angle = []
            ran = []
            curData = data.get(block=True, timeout=1)[0]
            for point in curData:
                [x, y] = transform_clustering(point)
                angle.append(x)
                ran.append(y)
            self.plotDataItem1.setData(angle, ran)

    def onNewData2(self):
        data = self.data[1]
        if data.qsize() > 7:
            self.timer2.setInterval(20)
        elif data.qsize() < 5:
            self.timer2.setInterval(100)
        if not data.empty():
            angle = []
            ran = []
            curData = data.get(block=True, timeout=1)
            for point in curData:
                [x, y] = transform_clustering(point)
                angle.append(x)
                ran.append(y)
            self.plotDataItem2.setData(angle, ran)

    def onNewData3(self):
        data = self.data[2]
        # print("showDataQueue3 size:", data.qsize())
        if data.qsize() > 15:
            self.timer3.setInterval(20)
        elif data.qsize() < 10:
            self.timer3.setInterval(100)
        if not data.empty():
            angle = []
            ran = []
            curData = data.get(block=True, timeout=1)
            for obj in curData:
                for point in obj:
                    [x, y] = transform_clustering(point)
                    angle.append(x)
                    ran.append(y)
            self.plotDataItem3.setData(angle, ran)

    def onNewData4(self):
        data = self.data[3]
        # print("showDataQueue4 size:", data.qsize())
        if data.qsize() > 15:
            self.timer4.setInterval(20)
        elif data.qsize() < 10:
            self.timer4.setInterval(100)
        if not data.empty():
            angle = []
            ran = []
            # 这里的data是聚类对象的显示队列
            curData = data.get(block=True, timeout=1)
            for obj in curData:
                for point in obj:
                    [x, y] = transform_clustering(point)
                    angle.append(x)
                    ran.append(y)
            self.plotDataItem4.setData(angle, ran)


class MyQtWidgets(threading.Thread):
    def __init__(self, *data):
        time.sleep(0.05)
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        app = QtWidgets.QApplication([])
        pg.setConfigOptions(antialias=False)  # True seems to work as well
        win = MyWidget(self.data)
        win.show()
        win.resize(700, 700)
        win.raise_()
        app.exec_()
