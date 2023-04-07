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

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Figure of Time Means - 20140626_180142')
    ax.set_xlabel('Space Point')
    ax.set_ylabel('Time Mean')
    plt.plot(np.arange(23493), data_mean, 'k-', color='k')
    plt.show()
