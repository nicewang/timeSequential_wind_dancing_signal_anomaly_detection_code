import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = '1.txt'
    data = np.genfromtxt(path)
    data = np.array(data)
#    data = data[0:71,:]

    i = data.shape
    j = i[0]
    k = i[1]

    data = data.reshape(j*k,)
#    data_max = data.max
#    data = data/data_max

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('One-Point Waving Plot Within 24 Hours')
    ax.set_xlabel('Time / h')
    ax.set_ylabel('Amplitude / V')
    plt.plot(np.arange(0, 24, 24.0/(j*k)), data, 'k-', color='b')
    plt.show()
