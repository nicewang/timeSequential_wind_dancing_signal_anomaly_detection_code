import numpy as np
import os
import sys

if __name__ == '__main__':
    path = '20140626_180142CH1.txt'
    path_in = sys.argv[1]
    data = np.genfromtxt(path_in)
    data = np.array(data)
    data = np.transpose(data)
    data = np.diff(data)
    data = data.std(1)
    print data.shape
    print data

    if os.path.exists('timeStd/timeStd.txt'):
        data1 = np.genfromtxt('timeStd/timeStd.txt')
        data_new = np.row_stack((data1, data))
        print data_new.shape
        np.savetxt('timeStd/timeStd.txt', data_new)
    else:
        np.savetxt('timeStd/timeStd.txt', data)
