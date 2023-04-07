import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    path = '2017061523_CH01.txt'
    # data=pd.read_csv(path)
    k = 23493
    fs = 7198.0/3600

    data = np.genfromtxt(path)
    data = np.array(data)
    data = data[:,1:150001]

    data = np.transpose(data)
    data = np.diff(data)

    data = fft(data,axis=1)
    data = abs(data)
    print data.shape

    data = data[:,3599:7198]
    print data.shape

    i = np.arange(0, 30000, 2)
    j = np.arange(0, fs/2, fs/(3599*2))
    #j = np.arange(-fs/2, fs/2, fs/(7199))
    i, j = np.meshgrid(j, i)
    print i.shape, j.shape

    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(i, j, data, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.set_xlabel('Frequency / Hz')
    ax.set_ylabel('Space / m')
    ax.set_zlabel('Amplitude / V')
    ax.set_title('Frequency Spectrogram - 20170615 23 to 24')

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
