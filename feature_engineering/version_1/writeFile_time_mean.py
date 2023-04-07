import numpy as np
import os
import sys

if __name__ == '__main__':
    path = '20140626_180142CH1.txt'
    path_in = sys.argv[1]
    data_original = np.genfromtxt(path_in)
    data_mean = np.array(data_original)
    data_mean = data_mean.mean(0)
    print data_mean.shape
    print data_mean

    if os.path.exists('time_mean/time_mean.txt'):
        data1 = np.genfromtxt('time_mean/time_mean.txt')
        data_new = np.row_stack((data1, data_mean))
        print data_new.shape
        np.savetxt('time_mean/time_mean.txt', data_new)
    else:
        np.savetxt('time_mean/time_mean.txt', data_mean)
