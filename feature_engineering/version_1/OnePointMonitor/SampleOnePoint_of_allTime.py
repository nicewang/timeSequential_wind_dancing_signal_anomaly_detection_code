import numpy as np
import sys
import os

if __name__ == '__main__':
    path = sys.argv[1]
    data = np.genfromtxt(path)
    data = np.array(data)
    data_10km = data[:,5000:5001]
    data_13km = data[:,6500:6501]
    data_33km = data[:,16500:16501]

    if os.path.exists('OnePointData_10km.txt'):
        data1 = np.genfromtxt('OnePointData_10km.txt')
        data_10km_new = np.column_stack((data1, data_10km))
        print '10km:'
        print data_10km_new
        print data_10km_new.shape
        np.savetxt('OnePointData_10km.txt', data_10km_new)
    else:
        print '10km:'
        print data_10km
        print data_10km.shape
        np.savetxt('OnePointData_10km.txt', data_10km)

    if os.path.exists('OnePointData_13km.txt'):
        data2 = np.genfromtxt('OnePointData_13km.txt')
        data_13km_new = np.column_stack((data2, data_13km))
        print '13km:'
        print data_13km_new
        print data_13km_new.shape
        np.savetxt('OnePointData_13km.txt', data_13km_new)
    else:
        print '13km:'
        print data_13km
        print data_13km.shape
        np.savetxt('OnePointData_13km.txt', data_13km)

    if os.path.exists('OnePointData_33km.txt'):
        data3 = np.genfromtxt('OnePointData_33km.txt')
        data_33km_new = np.column_stack((data3, data_33km))
        print '33km:'
        print data_33km_new
        print data_33km_new.shape
        np.savetxt('OnePointData_33km.txt', data_33km_new)
    else:
        print '33km:'
        print data_33km
        print data_33km.shape
        np.savetxt('OnePointData_33km.txt', data_33km)
