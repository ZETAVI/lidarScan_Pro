import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

theta = np.arange(0, 2*np.pi, 2*np.pi/100)
ax.plot(np.cos(theta), np.sin(theta))

plt.style.use('ggplot')
ax.set_xticks([-2, 2])
ax.set_yticks([-2, 2])


a = np.random.uniform(-1,1, [500,2])
for i in range(500):
    # ax.cla()
    plt.plot(a[i][0], a[i][1],'x')
    ax.legend()
    plt.pause(0.1)

plt.show()