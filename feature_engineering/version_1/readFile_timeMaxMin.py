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
    data_max = data.max(1)
    print data_max.shape
    print data_max
    data_min = data.min(1)
    print data_min.shape
    print data_min
    data_new = data_max - data_min
    print data_new.shape
    print data_new

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Figure of Time Peak-to-peaks - 20140626_180142')
    ax.set_xlabel('Space Point')
    ax.set_ylabel('Time Peak-to-peak')
    plt.plot(np.arange(23493), data_new, 'k-', color='r')
    plt.show()
