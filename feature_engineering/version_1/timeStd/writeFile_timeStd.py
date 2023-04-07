import numpy as np
import os
import sys

if __name__ == '__main__':
    path = 'timeStd.txt'
    path_in = sys.argv[1]
    data = np.genfromtxt(path_in)
    data = np.array(data)
    data = data.max(0)

    if os.path.exists('timeStd_Max_per_2Hours_per_SpacePoint.txt'):
        data1 = np.genfromtxt('timeStd_Max_per_2Hours_per_SpacePoint.txt')
        data_new = np.row_stack((data1, data))
        print data_new
        print data_new.shape
        np.savetxt('timeStd_Max_per_2Hours_per_SpacePoint.txt', data_new)
    else:
        print data
        print data.shape
        np.savetxt('timeStd_Max_per_2Hours_per_SpacePoint.txt', data)
