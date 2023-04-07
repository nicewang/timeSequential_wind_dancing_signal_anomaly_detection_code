import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    path = 'OnePoint/OnePointData_10km.txt'

    fs = 316943.0 / (60*60*24)
    print fs

    data = np.genfromtxt(path)
    data = np.array(data)
    data = np.transpose(data)
    data = data.reshape(852 * 372)
    data = np.diff(data)

    data = fft(data)
    data = abs(data)
    data = data[158471:316943]

    i = np.arange(0, fs / 2, fs / (2*(316943-158471)))

    plt.xlabel('Frequency / Hz')
    plt.ylabel('Amplitude / V')
    plt.title('Frequency Spectrogram of Point at 10km')

    plt.plot(i, data, color='purple')

    plt.show()
