import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = '20140626_180142CH1.txt'
    # data=pd.read_csv(path)
    data = np.genfromtxt(path)
    data = np.array(data)
    print data.shape
    print data
    data = np.transpose(data)
    print data.shape
    print data
    data = np.diff(data)
    print data.shape
    print data
    data = data.std(1)
    print data.shape
    print data

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Figure of Standard Deviations - 20140626_180142')
    ax.set_xlabel('Space Point')
    ax.set_ylabel('Standard Deviation')
    plt.plot(np.arange(23493), data, 'k-', color='b')
    plt.show()
