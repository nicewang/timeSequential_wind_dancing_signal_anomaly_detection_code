import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    path = '2017061507_CH01.txt'
    data = np.genfromtxt(path)
    data = np.array(data)
    data = data[:, 1:15001]
    print (data.shape)
    data = np.transpose(data)
    data = np.diff(data)
    print (data.shape)

    j = np.arange(0, 7198)
    i = np.arange(0, 30000, 2)
    i, j = np.meshgrid(j, i)

    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(i, j, data, cmap=cm.get_cmap('YlGnBu'), linewidth=0, antialiased=False)
#    surf = ax.plot_surface(i, j, data, cmap=cm.get_cmap('Paired'), linewidth=0, antialiased=False)
#    surf = ax.plot_surface(i, j, data, cmap=cm.get_cmap('RdYlBu_r'), linewidth=0, antialiased=False)
#    surf = ax.plot_surface(i, j, data, cmap=cm.get_cmap('Spectral_r'), linewidth=0, antialiased=False)

    ax.set_xlabel('Space / m')
    ax.set_ylabel('Time / h')
    ax.set_zlabel('Amplitude / V')
#    ax.set_title('Time-Domain Plot - 20140627_22_24')
    ax.set_title('Time-Domain Plot - Differential Std - 20140615_07_08')

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
