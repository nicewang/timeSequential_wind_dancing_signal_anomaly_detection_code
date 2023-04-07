import numpy as np
from sklearn import cluster

if __name__ == '__main__':
    data1 = np.array([[1, 2, 3], [7, 8, 9]])
    data2 = np.array([4, 5, 6])
    print data1.shape
    print data1
    print data2.shape
    print data2

    data3 = np.row_stack((data1, data2))

#    data3 = np.array([data1, data2])
    print data3

    i = data3.shape
    i1 = i[0]
    i2 = i[1]
    data4 = data3.reshape(i1*i2,)
    print data4

    data5 = np.zeros([71, 23493], dtype=np.int16)

    data5[0][0] = 1
    data5[70][23492] = 555

    print data5

    data6 = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    print 'data6:'
    print data6
    data6 = np.transpose(data6)
    print 'data6_transpose:'
    print data6
    data6 = data6.reshape(9,)
    print 'data6_reshape:'
    print data6
