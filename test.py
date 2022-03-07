import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# f=open('point cloud.txt','r')
f = open('C:/Users/shmily/Desktop/data.txt', 'r')
point = f.read()
f.close()
l1 = point.replace('\n', ',')
l2 = l1.split(',')
# l2.pop()
# print(l2)
m1 = np.array(l2[0:332199])
print(len(m1))
m2=m1.reshape(265565,4)
# m2 = m1.reshape(110733, 3)
print(m2)
m3 = []
for each in m2:
    each_line = list(map(lambda x: float(x), each))
    m3.append(each_line)
m4 = np.array(m3)

x = [k[0] for k in m4]
y = [k[1] for k in m4]
z = [k[2] for k in m4]

fig = plt.figure(dpi=120)
ax = fig.add_subplot(111, projection='3d')
plt.title('point cloud')
ax.scatter(x, y, z, c='b', marker='.', s=2, linewidth=0, alpha=1, cmap='spectral')

# ax.set_facecolor((0,0,0))
ax.axis('scaled')
# ax.xaxis.set_visible(False) 
# ax.yaxis.set_visible(False) 
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
