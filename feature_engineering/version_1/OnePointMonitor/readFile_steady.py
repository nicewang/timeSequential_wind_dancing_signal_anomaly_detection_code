import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = 'OnePoint/OnePointData_33km.txt'

    data = np.genfromtxt(path)
    data = np.array(data)
    data = np.transpose(data)
    data = data.reshape(852*372)
    data = np.diff(data)

    plt.plot(np.arange(0, 24, 24.0/(852*372-1)), data)
    plt.xlabel('Time / h')
    plt.ylabel('Amplitude / V')
    plt.title('Waving Situation of Point at 33km within 24 Hours')
    plt.show()
