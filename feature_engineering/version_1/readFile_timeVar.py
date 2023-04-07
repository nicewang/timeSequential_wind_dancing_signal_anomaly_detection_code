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
    data = data.var(1)
    print data.shape
    print data

    fig = plt.figure()
    plt.plot(np.arange(23493), data, 'k-', color='y')
    plt.show()
