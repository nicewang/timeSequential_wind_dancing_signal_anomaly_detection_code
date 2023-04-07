import numpy as np
import os
import sys

if __name__ == '__main__':
    path = '20140628_120100CH1.txt'
    path_in = sys.argv[1]
    data = np.genfromtxt(path_in)
    data = np.array(data)
    data = np.transpose(data)
    print data.shape
    print data

    if os.path.exists('txt_out/1.txt'):
        data1 = np.genfromtxt('txt_out/1.txt')

#        i = data[0].shape
#        i1 = data1.shape
#        i_new = i[0] + i1[0]

        data_new = np.row_stack((data1, data[0]))
        print data_new.shape
#        data_new = data_new.reshape(i_new, )
        np.savetxt('txt_out/1.txt', data_new)
    else:
        np.savetxt('txt_out/1.txt', data[0])
