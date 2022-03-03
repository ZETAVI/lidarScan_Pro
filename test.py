# import matplotlib.pyplot as plt
# import numpy as np
#
# """
# 20:以20作为半径
# ylim(0,100):设置极轴的范围
# lw=2:表示极坐标图案的宽度
# ro:绘制的极坐标图形为红色圆点
# """
#
# plt.polar(0.25 * np.pi, 0.1, "ro", lw=2)
# plt.ylim(0, 5)
# plt.show()
import time
import numpy as np
from matplotlib import pyplot as plt
import ydlidar

if __name__ == "__main__":
    ydlidar.os_init();
    ports = ydlidar.lidarPortList();
    port = "/dev/ydlidar";
    for key, value in ports.items():
        port = value;
    laser = ydlidar.CYdLidar();
    laser.setlidaropt(ydlidar.LidarPropSerialPort, port);
    laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 115200);
    laser.setlidaropt(ydlidar.LidarPropLidarType, ydlidar.TYPE_TRIANGLE);
    laser.setlidaropt(ydlidar.LidarPropDeviceType, ydlidar.YDLIDAR_TYPE_SERIAL);
    laser.setlidaropt(ydlidar.LidarPropScanFrequency, 10.0);
    laser.setlidaropt(ydlidar.LidarPropSampleRate, 3);
    laser.setlidaropt(ydlidar.LidarPropSingleChannel, True);
    laser.setlidaropt(ydlidar.LidarPropMaxAngle, 180.0);
    laser.setlidaropt(ydlidar.LidarPropMinAngle, -180.0);
    laser.setlidaropt(ydlidar.LidarPropMaxRange, 8.0);
    laser.setlidaropt(ydlidar.LidarPropMinRange, 0.08);



    ret = laser.initialize();
    if ret:
        ret = laser.turnOn();
        scan = ydlidar.LaserScan();
        while ret and ydlidar.os_isOk():
            r = laser.doProcessSimple(scan);
            if r:
                x = []
                y = []
                for point in scan.points:
                    x.append(point.range * np.sin(point0.angle))
                    y.append(point.range * np.cos(point.angle))
                plt.clf()
                plt.scatter(x, y)
                plt.pause(.1)
                plt.show()
            else:
                print("Failed to get Lidar Data")
            # time.sleep(0.05);
        laser.turnOff()
    laser.disconnecting()
#
# for i in range(1000000):
#     if i % 7 == 0:
#         x = []
#         y = []
#     print(i)
#     current_data = get_data()
#     for point in current_data:
#         if point[0] == 15:
#             x.append(point[2] * np.sin(point[1]))
#             y.append(point[2] * np.cos(point[1]))
#     plt.clf()
#     plt.scatter(x, y)
#     plt.pause(.1)
# plt.show()
