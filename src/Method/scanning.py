# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> scanning
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-02 16:02
    @Desc   :扫描单元
            获取雷达扫描仪的数据，添加到队列中
-------------------------------------------------
   Change Activity:
                   2022-03-02 16:02:
-------------------------------------------------
"""
__author__ = 'bobi'

import threading

import ydlidar

import time


class scanning:
    """雷达数据扫描"""
    laser = None

    def __init__(self, dataQueue, flag):
        self.MaxL = dataQueue.maxsize
        self.dataQueue = dataQueue
        self.flag = flag
        scanThread = threading.Thread(target=self.scan, )
        # 启动线程
        scanThread.start()

    # 启动线程扫描数据
    def scan(self):
        ydlidar.os_init()
        ports = ydlidar.lidarPortList()
        port = "/dev/ydlidar"
        for key, value in ports.items():
            port = value
        self.laser = ydlidar.CYdLidar()
        self.laser.setlidaropt(ydlidar.LidarPropSerialPort, port)
        self.laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 115200)
        self.laser.setlidaropt(ydlidar.LidarPropLidarType, ydlidar.TYPE_TRIANGLE)
        self.laser.setlidaropt(ydlidar.LidarPropDeviceType, ydlidar.YDLIDAR_TYPE_SERIAL)
        self.laser.setlidaropt(ydlidar.LidarPropScanFrequency, 10.0)
        self.laser.setlidaropt(ydlidar.LidarPropSampleRate, 3)
        self.laser.setlidaropt(ydlidar.LidarPropSingleChannel, True)
        self.laser.setlidaropt(ydlidar.LidarPropMaxAngle, 180.0)
        self.laser.setlidaropt(ydlidar.LidarPropMinAngle, -180.0)
        self.laser.setlidaropt(ydlidar.LidarPropMaxRange, 8.0)
        self.laser.setlidaropt(ydlidar.LidarPropMinRange, 0.08)
        ret = self.laser.initialize()
        if ret:
            ret = self.laser.turnOn()
            scan = ydlidar.LaserScan()
            print("start scanning ! press any key to stop")

            while ret and ydlidar.os_isOk() and self.flag[0]:
                r = self.laser.doProcessSimple(scan)
                if r:
                    # print("Scan received[", scan.stamp, "]:", scan.points.size(), "ranges is [",
                    #       1.0 / scan.config.scan_time, "]Hz")

                    # 将一个周期内的点集数据存入data
                    # print(self.dataQueue.qsize())
                    # for point in scan.points:
                    #     print(point.angle)
                    self.dataQueue.put(item=(scan.points,), block=True, timeout=1)
                else:
                    print("Failed to get Lidar Data")
                if self.dataQueue.qsize() < self.MaxL * 3 / 4:
                    pass
                    time.sleep(0.05)
                else:
                    print("Too many points in List")
                    time.sleep(0.2)
            self.laser.turnOff()
            print("lidar stop scan")

        self.laser.disconnecting()

    # def onKeyboardEvent(event):
    #
    #     # 监听键盘事件
    #     print("MessageName:", event.MessageName)
    #     print("---")
    #     # 同鼠标事件监听函数的返回值
    #     return True
