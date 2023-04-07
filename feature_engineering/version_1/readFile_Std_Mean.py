import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':
    path = '20140626_180142CH1.txt'
    path_in = sys.argv[1]
    path_out = sys.argv[2]
    print path
    print path_in
    print path_out
    # data=pd.read_csv(path)
    data_original = np.genfromtxt(path_in)
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
    data = data.std(1)
    print data.shape
    print data

    data_rate = data / data_mean
    data_rate_max = data_rate.max()
    data_rate = data_rate / data_rate_max

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Figure of Standard-Deviations/Time_means')
    ax.set_xlabel('Space Point')
    ax.set_ylabel('Standard-Deviation/Time_mean')
#    plt.plot(np.arange(23493), data_mean, 'k-', color='k')
#    plt.plot(np.arange(23493), data, 'k-', color='b')
    plt.plot(np.arange(23493), data_rate, 'k-', color='#6495ED')
    plt.savefig(path_out)
#    plt.show()
