import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    path = 'SamplePoints_everyKm_start_at_0km_22_24.txt'
    # data=pd.read_csv(path)
    k = 23493
    fs = 371.0/100

    data = np.genfromtxt(path)
    data = np.array(data)
    print data.shape
#    print data

#    data = data[:,0:12000]
#    print data.shape
#    print data

    data = np.transpose(data)
    data = np.diff(data)

    data = fft(data,axis=1)
#    print data[:,10]
    data = abs(data)
#    print data[:,10]
    print data.shape

    data = data[:,13205:26411]
    print data.shape
    print data

    data = np.transpose(data)

#    i = np.arange(0, 47, 1)
    j = np.arange(0, 47, 1)
#    j = np.arange(0, fs/2, fs/(13206*2))
    i = np.arange(0, fs / 2, fs / (13206 * 2))
    i, j = np.meshgrid(j, i)
    print i.shape, j.shape

    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(i, j, data, cmap=cm.coolwarm, linewidth=0, antialiased=False)

#    ax.set_xlabel('Frequency / Hz')
    ax.set_ylabel('Frequency / Hz')
#    ax.set_ylabel('Space / km')
    ax.set_xlabel('Space / km')
    ax.set_zlabel('Amplitude / V')
    ax.set_title('Frequency Spectrogram - Sample Points per Kilometer Start at 0km - between 22 and 24 - (2)')

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
