import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = '20140626_180142CH1.txt'
    # data=pd.read_csv(path)
    data_original = np.genfromtxt(path)
    data_mean = np.array(data_original)
    print data_mean.shape
    print data_mean
    data_mean = data_mean.mean(0)
    print data_mean.shape
    print data_mean

    data = np.array(data_original)
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

    data_rate = data_new / data_mean
    data_rate_max = data_rate.max()
    data_rate = data_rate / data_rate_max

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Figure of Peak-to-peaks/Time_means - 20140626_180142')
    ax.set_xlabel('Space Point')
    ax.set_ylabel('Peak-to-peak/Time_mean')
#    plt.plot(np.arange(23493), data_mean, 'k-', color='k')
#    plt.plot(np.arange(23493), data_new, 'k-', color='r')
    plt.plot(np.arange(23493), data_rate, 'k-', color='#DEB887')
    plt.show()
