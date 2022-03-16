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

from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
from src.Method.globalFunc import transform


class MyWidget(pg.GraphicsWindow):

    def __init__(self, dataQueue, parent=None):
        # time.sleep(5)
        super().__init__(parent=parent)
        self.dataQueue = dataQueue
        # 画图初始化
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(115)  # in milliseconds
        self.timer.start()
        self.timer.timeout.connect(self.onNewData)
        self.plotItem = self.addPlot(title="Lidar points")
        self.plotDataItem = self.plotItem.plot([], pen=None, symbolBrush=(255, 0, 0), symbolSize=5, symbolPen=None)

    def setData(self, x, y):
        self.plotDataItem.setData(x, y)

    # todo dataQueue改为objectQueue
    def onNewData(self):
        if not self.dataQueue.empty():
            angle = []
            ran = []
            curData = self.dataQueue.get(block=True, timeout=1)[0]
            for point in curData:
                [x, y] = transform(point)
                angle.append(x)
                ran.append(y)
            self.setData(angle, ran)


class MyQtWidgets(threading.Thread):
    def __init__(self, dataQueue):
        time.sleep(0.05)
        threading.Thread.__init__(self)
        self.dataQueue = dataQueue

    def run(self):
        app = QtWidgets.QApplication([])
        pg.setConfigOptions(antialias=False)  # True seems to work as well
        win = MyWidget(self.dataQueue)
        win.show()
        win.resize(700, 700)
        win.raise_()
        app.exec_()
