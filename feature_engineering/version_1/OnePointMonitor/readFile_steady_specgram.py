import matplotlib.pyplot as plt
from pylab import *

if __name__ == '__main__':
    path = 'OnePoint/OnePointData_33km.txt'

    fs = 316943.0 / (60*60*24)
    print fs

    data = np.genfromtxt(path)
    data = np.array(data)
    data = np.transpose(data)
    data = data.reshape(852 * 372)
    data = np.diff(data)

#    data = fft(data)
#    data = abs(data)

    specgram(data, NFFT=1024, Fs=fs, noverlap=900)
    plt.xlabel('Time Point No.')
    plt.ylabel('Frequency / Hz')
    plt.title('Specgram of Waving Situation of Point at 33km within 24 Hours')
    show()