import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':
    path = sys.argv[1]
    data = np.genfromtxt(path)
    data = np.array(data)
    data = np.diff(data)
    data_o = data
    data = np.fft.rfft(data)
    data = abs(data)

    fs = data.shape[0]
    fs = fs / (24*3600.0)
    print fs

    #data1 = data[86396:172792]

    #plt.plot(np.arange(0, fs/2, fs/(data.shape[0])), data, color='blue')
    plt.figure(figsize=(7,4))
    plt.plot(np.fft.rfftfreq(len(data_o)), data, color='blue')
    plt.xlabel('Frequency / Hz')
    plt.ylabel('Amplitude / V')
    plt.title('Frequency Plot of Space Point at ' + str(path).split('_')[4].split('.')[0] + '.' + str(path).split('_')[4].split('.')[1])
    title = 'Frequency Plot of Space Point at ' + str(path).split('_')[4].split('.')[0] + '.' + str(path).split('_')[4].split('.')[1]
    title = title + '.jpg'
    title = 'picFreq/' + title
    print title
    #plt.savefig(title)
    plt.show()
