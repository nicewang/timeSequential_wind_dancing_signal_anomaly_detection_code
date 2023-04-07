# -*- coding: utf-8 -*-
import os
import numpy as np

def getOnePointDataOriginal(path):
    data = np.genfromtxt(path)
    data = np.array(data)
    data = data[:, 1:15001]
    print(data.shape)

    count = 0
    for i in range(1550, 6550, 250):
        data1 = data[:, i:i + 1]
        if count == 0:
            data_3km100 = data1
            count = count + 1
            continue
        if count == 1:
            data_3km600 = data1
            count = count + 1
            continue
        if count == 2:
            data_4km100 = data1
            count = count + 1
            continue
        if count == 3:
            data_4km600 = data1
            count = count + 1
            continue
        if count == 4:
            data_5km100 = data1
            count = count + 1
            continue
        if count == 5:
            data_5km600 = data1
            count = count + 1
            continue
        if count == 6:
            data_6km100 = data1
            count = count + 1
            continue
        if count == 7:
            data_6km600 = data1
            count = count + 1
            continue
        if count == 8:
            data_7km100 = data1
            count = count + 1
            continue
        if count == 9:
            data_7km600 = data1
            count = count + 1
            continue
        if count == 10:
            data_8km100 = data1
            count = count + 1
            continue
        if count == 11:
            data_8km600 = data1
            count = count + 1
            continue
        if count == 12:
            data_9km100 = data1
            count = count + 1
            continue
        if count == 13:
            data_9km600 = data1
            count = count + 1
            continue
        if count == 14:
            data_10km100 = data1
            count = count + 1
            continue
        if count == 15:
            data_10km600 = data1
            count = count + 1
            continue
        if count == 16:
            data_11km100 = data1
            count = count + 1
            continue
        if count == 17:
            data_11km600 = data1
            count = count + 1
            continue
        if count == 18:
            data_12km100 = data1
            count = count + 1
            continue
        if count == 19:
            data_12km600 = data1
            count = 0
            continue

    print('3.1km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_3.1km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_3.1km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_3km100))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_3.1km.txt', data_new_2)
    else:
        print(data_3km100)
        print(data_3km100.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_3.1km.txt', data_3km100)

    print('3.6km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_3.6km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_3.6km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_3km600))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_3.6km.txt', data_new_2)
    else:
        print(data_3km600)
        print(data_3km600.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_3.6km.txt', data_3km600)

    print('4.1km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_4.1km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_4.1km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_4km100))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_4.1km.txt', data_new_2)
    else:
        print(data_4km100)
        print(data_4km100.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_4.1km.txt', data_4km100)

    print('4.6km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_4.6km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_4.6km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_4km600))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_4.6km.txt', data_new_2)
    else:
        print(data_4km600)
        print(data_4km600.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_4.6km.txt', data_4km600)

    print('5.1km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_5.1km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_5.1km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_5km100))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_5.1km.txt', data_new_2)
    else:
        print(data_5km100)
        print(data_5km100.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_5.1km.txt', data_5km100)

    print('5.6km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_5.6km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_5.6km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_5km600))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_5.6km.txt', data_new_2)
    else:
        print(data_5km600)
        print(data_5km600.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_5.6km.txt', data_5km600)

    print('6.1km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_6.1km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_6.1km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_6km100))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_6.1km.txt', data_new_2)
    else:
        print(data_6km100)
        print(data_6km100.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_6.1km.txt', data_6km100)

    print('6.6km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_6.6km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_6.6km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_6km600))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_6.6km.txt', data_new_2)
    else:
        print(data_6km600)
        print(data_6km600.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_6.6km.txt', data_6km600)

    print('7.1km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_7.1km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_7.1km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_7km100))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_7.1km.txt', data_new_2)
    else:
        print(data_7km100)
        print(data_7km100.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_7.1km.txt', data_7km100)

    print('7.6km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_7.6km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_7.6km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_7km600))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_7.6km.txt', data_new_2)
    else:
        print(data_7km600)
        print(data_7km600.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_7.6km.txt', data_7km600)

    print('8.1km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_8.1km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_8.1km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_8km100))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_8.1km.txt', data_new_2)
    else:
        print(data_8km100)
        print(data_8km100.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_8.1km.txt', data_8km100)

    print('8.6km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_8.6km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_8.6km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_8km600))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_8.6km.txt', data_new_2)
    else:
        print(data_8km600)
        print(data_8km600.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_8.6km.txt', data_8km600)

    print('9.1km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_9.1km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_9.1km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_9km100))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_9.1km.txt', data_new_2)
    else:
        print(data_9km100)
        print(data_9km100.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_9.1km.txt', data_9km100)

    print('9.6km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_9.6km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_9.6km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_9km600))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_9.6km.txt', data_new_2)
    else:
        print(data_9km600)
        print(data_9km600.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_9.6km.txt', data_9km600)

    print('10.1km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_10.1km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_10.1km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_10km100))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_10.1km.txt', data_new_2)
    else:
        print(data_10km100)
        print(data_10km100.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_10.1km.txt', data_10km100)

    print('10.6km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_10.6km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_10.6km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_10km600))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_10.6km.txt', data_new_2)
    else:
        print(data_10km600)
        print(data_10km600.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_10.6km.txt', data_10km600)

    print('11.1km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_11.1km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_11.1km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_11km100))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_11.1km.txt', data_new_2)
    else:
        print(data_11km100)
        print(data_11km100.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_11.1km.txt', data_11km100)

    print('11.6km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_11.6km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_11.6km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_11km600))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_11.6km.txt', data_new_2)
    else:
        print(data_11km600)
        print(data_11km600.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_11.6km.txt', data_11km600)

    print('12.1km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_12.1km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_12.1km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_12km100))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_12.1km.txt', data_new_2)
    else:
        print(data_12km100)
        print(data_12km100.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_12.1km.txt', data_12km100)

    print('12.6km:')
    if os.path.exists('original_onePointData/Data_of_Point_at_12.6km.txt'):
        data1 = np.genfromtxt('original_onePointData/Data_of_Point_at_12.6km.txt')
        data1 = data1.reshape(data1.shape[0], 1)
        data_new_2 = np.vstack((data1, data_12km600))
        print(data_new_2)
        print(data_new_2.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_12.6km.txt', data_new_2)
    else:
        print(data_12km600)
        print(data_12km600.shape)
        np.savetxt('original_onePointData/Data_of_Point_at_12.6km.txt', data_12km600)
