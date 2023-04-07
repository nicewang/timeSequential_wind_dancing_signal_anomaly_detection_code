import numpy as np
import sys
import os

if __name__ == '__main__':
    path = sys.argv[1]
    data = np.genfromtxt(path)
    data = np.array(data)

    data_new = []
    for i in xrange(0, 23493, 500):
        data1 = data[:, i:i + 1]
        if data_new == []:
            data_new = data1
        else:
            data_new = np.column_stack((data_new, data1))

    if os.path.exists('SamplePoints_everyKm_start_at_0km_2_4.txt'):
        data1 = np.genfromtxt('SamplePoints_everyKm_start_at_0km_2_4.txt')
        data_new_2 = np.row_stack((data1, data_new))
        print data_new_2
        print data_new_2.shape
        np.savetxt('SamplePoints_everyKm_start_at_0km_2_4.txt', data_new_2)
    else:
        print data_new
        print data_new.shape
        np.savetxt('SamplePoints_everyKm_start_at_0km_2_4.txt', data_new)
