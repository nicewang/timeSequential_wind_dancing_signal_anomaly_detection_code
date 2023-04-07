import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    path = '20140628_120100CH1.txt'
    # data=pd.read_csv(path)
    k = 23493
    data = np.genfromtxt(path)
    data = np.array(data)
    print data.shape
    print data

    data = data[:,0:12000]
    print data.shape
    print data

    data = np.transpose(data)
    data = np.diff(data)

    i = np.arange(0, 24000, 2)
    j = np.arange(0, 100, 100.0/371)
    i, j = np.meshgrid(j, i)
    print i.shape, j.shape

    fig = plt.figure()
    ax = Axes3D(fig)
#    ax.scatter(i, j, data, depthshade=False)
    surf = ax.plot_surface(i, j, data, cmap=cm.get_cmap('Accent'), linewidth=0, antialiased=False)

    ax.set_xlabel('Time / s')
    ax.set_ylabel('Space / m')
    ax.set_zlabel('Amplitude / V')
    ax.set_title('Time-Domain Plot - 20140628_120100')

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
