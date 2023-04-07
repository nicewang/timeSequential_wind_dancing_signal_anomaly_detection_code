import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    path = '2017061500_CH01.txt'
    data = np.genfromtxt(path)
    data = np.array(data)
    data = data[:, 1:15001]
    print (data.shape)

    data_new = []
    for i in np.arange(0, 7200, 100):
        data_tmp = data[i:i + 100, :]
        data_tmp = np.transpose(data_tmp)
        data_tmp = np.diff(data_tmp)
        data_tmp = data_tmp.std(1)
        if data_new == []:
            data_new = data_tmp
        else:
            data_new = np.row_stack((data_new, data_tmp))

    print (data_new.shape)
    #np.savetxt('timeStd/timeStd_2017061500.txt', data_new)
