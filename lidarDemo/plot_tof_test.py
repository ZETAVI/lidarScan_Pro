import matplotlib.animation as animation
import matplotlib.pyplot as plt
import ydlidar

RMAX = 32.0


fig = plt.figure()
fig.canvas.set_window_title('YDLidar LIDAR Monitor')
# 极坐标图
lidar_polar = plt.subplot(polar=True)
# 自动缩放
lidar_polar.autoscale(False)
# lidar_polar.autoscale_view(False, False, False)
lidar_polar.set_rmax(RMAX)
# 调整网格线
# lidar_polar.grid(True)
lidar_polar.grid(linestyle="--", color="black")

ports = ydlidar.lidarPortList()
port = "/dev/ydlidar"
for key, value in ports.items():
    port = value

laser = ydlidar.CYdLidar()
laser.setlidaropt(ydlidar.LidarPropSerialPort, port)
laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 115200)
laser.setlidaropt(ydlidar.LidarPropLidarType, ydlidar.TYPE_TRIANGLE)
laser.setlidaropt(ydlidar.LidarPropDeviceType, ydlidar.YDLIDAR_TYPE_SERIAL)
laser.setlidaropt(ydlidar.LidarPropScanFrequency, 10.0)
laser.setlidaropt(ydlidar.LidarPropSampleRate, 3)
laser.setlidaropt(ydlidar.LidarPropSingleChannel, True)
scan = ydlidar.LaserScan()


def animate(num):
    r = laser.doProcessSimple(scan)
    if r:
        angle = []
        ran = []
        intensity = []
        for point in scan.points:
            angle.append(point.angle)
            ran.append(point.range)
            intensity.append(point.intensity)
        lidar_polar.clear()
        lidar_polar.scatter(angle, ran, c=intensity, cmap='hsv', alpha=0.95)


ret = laser.initialize()
if ret:
    ret = laser.turnOn()
    if ret:
        ani = animation.FuncAnimation(fig, animate, interval=5)
        plt.show()
    laser.turnOff();
laser.disconnecting();
plt.close();
