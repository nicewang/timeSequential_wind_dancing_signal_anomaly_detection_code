import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = '20140628_120100CH1.txt'
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
    data = data.mean(1)
    print data.shape
    print data
    data = map(abs, data)
#    print data.shape
    print data

    path1 = '20140627_120157CH1.txt'
    data1 = np.genfromtxt(path1)
    data1 = np.array(data1)
    print data1.shape
    print data1
    data1 = np.transpose(data1)
    print data1.shape
    print data1
    data1 = np.diff(data1)
    print data1.shape
    print data1
    data1 = data1.mean(1)
    print data1.shape
    print data1
    data1 = map(abs, data1)
    #    print data1.shape
    print data1

    fig = plt.figure()
    plt.plot(np.arange(23493), data, 'k-', color='k')
    plt.plot(np.arange(23493), data1, 'k-', color='g')
    plt.show()
