import numpy as np
from numpy.fft import fft
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from pylab import *

if __name__ == '__main__':
    path = 'OnePoint/OnePointData_10km.txt'

    fs = 316943.0 / (60 * 60 * 24)

    data = np.genfromtxt(path)
    data = np.array(data)
    data = np.transpose(data)
    data = data.reshape(852 * 372)
    data = np.diff(data)

    data_fft = fft(data)
    data_fft = abs(data_fft)
    data_fft = data_fft[158471:316943]

    subplot(2, 2, 1)
    plot(np.arange(0, 24, 24.0/(852*372-1)), data, 'r')
    xlabel('Time / h')
    ylabel('Amplitude / V')
    grid()

#    i = np.arange(- fs / 2, fs / 2, fs / (316943))
    i = np.arange(0, fs / 2, fs / (2 * (316943 - 158471)))
    subplot(2, 2, 2)
    plot(i, data_fft, 'k')
    xlabel('Frequency / Hz')
    ylabel('Amplitude / V')
    grid()

    subplot(2, 2, 3)
    specgram(data, NFFT=1024, Fs=fs, noverlap=900)
    xlabel('Time Point No.')
    ylabel('Frequency / Hz')

    show()
