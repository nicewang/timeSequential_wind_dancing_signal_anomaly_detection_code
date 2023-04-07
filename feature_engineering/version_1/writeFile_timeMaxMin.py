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
    data_max = data.max(1)
    data_min = data.min(1)
    data_differential = data_max - data_min
    print data_differential.shape
    print data_differential

    if os.path.exists('timeMaxMin/timeMaxMin.txt'):
        data1 = np.genfromtxt('timeMaxMin/timeMaxMin.txt')
        data_new = np.row_stack((data1, data_differential))
        print data_new.shape
        np.savetxt('timeMaxMin/timeMaxMin.txt', data_new)
    else:
        np.savetxt('timeMaxMin/timeMaxMin.txt', data_differential)
