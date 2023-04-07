import sys
import os
import numpy as np
from scikits.talkbox.linpred import py_lpc

if __name__ == '__main__':
    path = sys.argv[1]
    data = np.genfromtxt(path)
    data = np.array(data)
    data = data[:, 1:15001]
    print data.shape

    data_0km100 = []
    data_3km100 = []
    data_6km100 = []
    data_9km100 = []
    data_12km100 = []
    data_15km100 = []
    data_18km100 = []
    data_21km100 = []
    data_24km100 = []
    data_27km100 = []
    for i in np.arange(0, 7200, 100):
        data_tmp = data[i:i + 100, :]
        data_tmp = np.transpose(data_tmp)
        data_tmp = np.diff(data_tmp)

        count = 0
        for j in xrange(50, 14000, 1500):
            data1 = data_tmp[j:j + 1,:]
            data1 = data1.reshape(data1.shape[0]*data1.shape[1])
            data1 = py_lpc.lpc_ref(data1, 10)
            print data1
            data1 = data1[1:]
            data1 = data1.mean(0)
            print data1
            if count == 0:
                if data_0km100 == []:
                    data_0km100 = data1
                else:
                    data_0km100 = np.row_stack((data_0km100, data1))
                count = count + 1
                continue
            if count == 1:
                if data_3km100 == []:
                    data_3km100 = data1
                else:
                    data_3km100 = np.row_stack((data_3km100, data1))
                count = count + 1
                continue
            if count == 2:
                if data_6km100 == []:
                    data_6km100 = data1
                else:
                    data_6km100 = np.row_stack((data_6km100, data1))
                count = count + 1
                continue
            if count == 3:
                if data_9km100 == []:
                    data_9km100 = data1
                else:
                    data_9km100 = np.row_stack((data_9km100, data1))
                count = count + 1
                continue
            if count == 4:
                if data_12km100 == []:
                    data_12km100 = data1
                else:
                    data_12km100 = np.row_stack((data_12km100, data1))
                count = count + 1
                continue
            if count == 5:
                if data_15km100 == []:
                    data_15km100 = data1
                else:
                    data_15km100 = np.row_stack((data_15km100, data1))
                count = count + 1
                continue
            if count == 6:
                if data_18km100 == []:
                    data_18km100 = data1
                else:
                    data_18km100 = np.row_stack((data_18km100, data1))
                count = count + 1
                continue
            if count == 7:
                if data_21km100 == []:
                    data_21km100 = data1
                else:
                    data_21km100 = np.row_stack((data_21km100, data1))
                count = count + 1
                continue
            if count == 8:
                if data_24km100 == []:
                    data_24km100 = data1
                else:
                    data_24km100 = np.row_stack((data_24km100, data1))
                count = count + 1
                continue
            if count == 9:
                if data_27km100 == []:
                    data_27km100 = data1
                else:
                    data_27km100 = np.row_stack((data_27km100, data1))
                count = 0
                continue

    print '0.1km:'
    if os.path.exists('lpc/SpacePoint/0.1km/lpc_of_Point_at_0.1km.txt'):
        data1 = np.genfromtxt('lpc/SpacePoint/0.1km/lpc_of_Point_at_0.1km.txt')
        data_new_2 = np.column_stack((data1, data_0km100))
        print data_new_2
        print data_new_2.shape
        np.savetxt('lpc/SpacePoint/0.1km/lpc_of_Point_at_0.1km.txt', data_new_2)
    else:
        print data_0km100
        print data_0km100.shape
        np.savetxt('lpc/SpacePoint/0.1km/lpc_of_Point_at_0.1km.txt', data_0km100)

    print '3.1km:'
    if os.path.exists('lpc/SpacePoint/3.1km/lpc_of_Point_at_3.1km.txt'):
        data1 = np.genfromtxt('lpc/SpacePoint/3.1km/lpc_of_Point_at_3.1km.txt')
        data_new_2 = np.column_stack((data1, data_3km100))
        print data_new_2
        print data_new_2.shape
        np.savetxt('lpc/SpacePoint/3.1km/lpc_of_Point_at_3.1km.txt', data_new_2)
    else:
        print data_3km100
        print data_3km100.shape
        np.savetxt('lpc/SpacePoint/3.1km/lpc_of_Point_at_3.1km.txt', data_3km100)

    print 'timeSeg:'
    if os.path.exists('lpc/SpacePoint/timeSeg/lpc_of_Point_at_6.1km.txt'):
        data1 = np.genfromtxt('lpc/SpacePoint/timeSeg/lpc_of_Point_at_6.1km.txt')
        data_new_2 = np.column_stack((data1, data_6km100))
        print data_new_2
        print data_new_2.shape
        np.savetxt('lpc/SpacePoint/timeSeg/lpc_of_Point_at_6.1km.txt', data_new_2)
    else:
        print data_6km100
        print data_6km100.shape
        np.savetxt('lpc/SpacePoint/timeSeg/lpc_of_Point_at_6.1km.txt', data_6km100)

    print '9.1km:'
    if os.path.exists('lpc/SpacePoint/9.1km/lpc_of_Point_at_9.1km.txt'):
        data1 = np.genfromtxt('lpc/SpacePoint/9.1km/lpc_of_Point_at_9.1km.txt')
        data_new_2 = np.column_stack((data1, data_9km100))
        print data_new_2
        print data_new_2.shape
        np.savetxt('lpc/SpacePoint/9.1km/lpc_of_Point_at_9.1km.txt', data_new_2)
    else:
        print data_9km100
        print data_9km100.shape
        np.savetxt('lpc/SpacePoint/9.1km/lpc_of_Point_at_9.1km.txt', data_9km100)

    print '12.1km:'
    if os.path.exists('lpc/SpacePoint/12.1km/lpc_of_Point_at_12.1km.txt'):
        data1 = np.genfromtxt('lpc/SpacePoint/12.1km/lpc_of_Point_at_12.1km.txt')
        data_new_2 = np.column_stack((data1, data_12km100))
        print data_new_2
        print data_new_2.shape
        np.savetxt('lpc/SpacePoint/12.1km/lpc_of_Point_at_12.1km.txt', data_new_2)
    else:
        print data_12km100
        print data_12km100.shape
        np.savetxt('lpc/SpacePoint/12.1km/lpc_of_Point_at_12.1km.txt', data_12km100)

    print '15.1km:'
    if os.path.exists('lpc/SpacePoint/15.1km/lpc_of_Point_at_15.1km.txt'):
        data1 = np.genfromtxt('lpc/SpacePoint/15.1km/lpc_of_Point_at_15.1km.txt')
        data_new_2 = np.column_stack((data1, data_15km100))
        print data_new_2
        print data_new_2.shape
        np.savetxt('lpc/SpacePoint/15.1km/lpc_of_Point_at_15.1km.txt', data_new_2)
    else:
        print data_15km100
        print data_15km100.shape
        np.savetxt('lpc/SpacePoint/15.1km/lpc_of_Point_at_15.1km.txt', data_15km100)

    print '18.1km:'
    if os.path.exists('lpc/SpacePoint/18.1km/lpc_of_Point_at_18.1km.txt'):
        data1 = np.genfromtxt('lpc/SpacePoint/18.1km/lpc_of_Point_at_18.1km.txt')
        data_new_2 = np.column_stack((data1, data_18km100))
        print data_new_2
        print data_new_2.shape
        np.savetxt('lpc/SpacePoint/18.1km/lpc_of_Point_at_18.1km.txt', data_new_2)
    else:
        print data_18km100
        print data_18km100.shape
        np.savetxt('lpc/SpacePoint/18.1km/lpc_of_Point_at_18.1km.txt', data_18km100)

    print '21.1km:'
    if os.path.exists('lpc/SpacePoint/21.1km/lpc_of_Point_at_21.1km.txt'):
        data1 = np.genfromtxt('lpc/SpacePoint/21.1km/lpc_of_Point_at_21.1km.txt')
        data_new_2 = np.column_stack((data1, data_21km100))
        print data_new_2
        print data_new_2.shape
        np.savetxt('lpc/SpacePoint/21.1km/lpc_of_Point_at_21.1km.txt', data_new_2)
    else:
        print data_21km100
        print data_21km100.shape
        np.savetxt('lpc/SpacePoint/21.1km/lpc_of_Point_at_21.1km.txt', data_21km100)

    print '24.1km:'
    if os.path.exists('lpc/SpacePoint/24.1km/lpc_of_Point_at_24.1km.txt'):
        data1 = np.genfromtxt('lpc/SpacePoint/24.1km/lpc_of_Point_at_24.1km.txt')
        data_new_2 = np.column_stack((data1, data_24km100))
        print data_new_2
        print data_new_2.shape
        np.savetxt('lpc/SpacePoint/24.1km/lpc_of_Point_at_24.1km.txt', data_new_2)
    else:
        print data_24km100
        print data_24km100.shape
        np.savetxt('lpc/SpacePoint/24.1km/lpc_of_Point_at_24.1km.txt', data_24km100)

    print '27.1km:'
    if os.path.exists('lpc/SpacePoint/27.1km/lpc_of_Point_at_27.1km.txt'):
        data1 = np.genfromtxt('lpc/SpacePoint/27.1km/lpc_of_Point_at_27.1km.txt')
        data_new_2 = np.column_stack((data1, data_27km100))
        print data_new_2
        print data_new_2.shape
        np.savetxt('lpc/SpacePoint/27.1km/lpc_of_Point_at_27.1km.txt', data_new_2)
    else:
        print data_27km100
        print data_27km100.shape
        np.savetxt('lpc/SpacePoint/27.1km/lpc_of_Point_at_27.1km.txt', data_27km100)
