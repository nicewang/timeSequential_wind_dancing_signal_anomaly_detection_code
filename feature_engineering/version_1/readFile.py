import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    path = '20140628_120100CH1.txt'
    # data=pd.read_csv(path)
    k = 23493
    data = np.genfromtxt(path)
    data = np.array(data)
    print data.shape
    print data

    data = data[:,0:1000]
    print data.shape
    print data

    i = np.arange(372)
    j = np.arange(1000)
    i, j = np.meshgrid(j, i)
    print i.shape, j.shape

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(i, j, data)
#    ax.plot_surface(i, j, data)
    plt.show()
