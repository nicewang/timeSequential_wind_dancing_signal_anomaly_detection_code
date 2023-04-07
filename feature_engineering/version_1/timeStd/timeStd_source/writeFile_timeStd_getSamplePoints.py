import numpy as np
import os
import sys

if __name__ == '__main__':
    path = 'timeStd.txt'
    path_in = sys.argv[1]
    data = np.genfromtxt(path_in)
    data = np.array(data)
    data_new = []
 #   for i in xrange(0,23493,500):
    for i in xrange(16250, 16750, 1):
        data1 = data[:, i:i + 1]
        if data_new == [] :
            data_new = data1
        else:
            data_new = np.column_stack((data_new,data1))

    #if os.path.exists('timeStd_SamplePoints_everyKm.txt'):
    if os.path.exists('SampleResults/timeStd_SamplePoints_32.5_33.5km.txt'):
        #data1 = np.genfromtxt('timeStd_SamplePoints_everyKm.txt')
        data1 = np.genfromtxt('SampleResults/timeStd_SamplePoints_32.5_33.5km.txt')
        data_new_2 = np.row_stack((data1, data_new))
        print data_new_2
        print data_new_2.shape
        #np.savetxt('timeStd_SamplePoints_everyKm.txt', data_new_2)
        np.savetxt('SampleResults/timeStd_SamplePoints_32.5_33.5km.txt', data_new_2)
    else:
        print data_new
        print data_new.shape
        #np.savetxt('timeStd_SamplePoints_everyKm.txt', data_new)
        np.savetxt('SampleResults/timeStd_SamplePoints_32.5_33.5km.txt', data_new)
