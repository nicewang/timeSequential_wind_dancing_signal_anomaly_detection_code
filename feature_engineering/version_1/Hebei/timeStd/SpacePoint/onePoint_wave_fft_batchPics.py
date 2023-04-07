import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import sys

if __name__ == '__main__':
    #path = sys.argv[1]
    path = '27.1km/timeStd_of_Point_at_27.1km.txt'
    data = np.genfromtxt(path)
    data = np.array(data)
    data = np.transpose(data)
    data = data.reshape(72 * 24)
    print data.shape
    print data
    data = fft(data, axis=0)
    data = abs(data)

    plt.plot(np.arange(0, 24, 24.0/(72*24)), data, color='brown')
    plt.xlabel('Time / Hour')
    plt.ylabel('Amplitude / V')
    plt.title('Frequency Plot of Space Point at ' + str(path).split('_')[4].split('.')[0] + '.' + str(path).split('_')[4].split('.')[1])
    title = 'Frequency Plot of Space Point at ' + str(path).split('_')[4].split('.')[0] + '.' + str(path).split('_')[4].split('.')[1]
    title = title + '.jpg'
    title = 'pic/frequencyPlot/' + title
    print title
    #plt.savefig(title)
    plt.show()