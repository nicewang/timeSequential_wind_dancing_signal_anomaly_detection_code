# -*- coding: utf-8 -*-
import os
import numpy as np

def getOnePointData(path):
    data = np.genfromtxt(path)
    data = np.array(data)
    data = data[:, 1:15001]
    print(data.shape)

    # 计算短时风舞最大值
    data_timeMax = []
    for i in range(0, 7200, 100):
        data_tmp = data[i:i + 100, :]
        data_tmp = np.transpose(data_tmp)
        data_tmp = np.diff(data_tmp)
        # data_tmp = map(abs, data_tmp)
        data_tmp = abs(data_tmp)
        # data_tmp = np.array(data_tmp)
        data_tmp = data_tmp.max(1)
        if data_timeMax == []:
            data_timeMax = data_tmp
        else:
            data_timeMax = np.row_stack((data_timeMax, data_tmp))

    # 计算短时风舞峰峰值
    data_timeMaxMin = []
    for i in range(0, 7200, 100):
        data_tmp = data[i:i + 100, :]
        data_tmp = np.transpose(data_tmp)
        data_tmp = np.diff(data_tmp)
        data_max = data_tmp.max(1)
        data_min = data_tmp.min(1)
        data_tmp = data_max - data_min
        if data_timeMaxMin == []:
            data_timeMaxMin = data_tmp
        else:
            data_timeMaxMin = np.row_stack((data_timeMaxMin, data_tmp))

    # 计算短时风舞时间均值
    data_timeMean = []
    for i in range(0, 7200, 100):
        data_tmp = data[i:i + 100, :]
        data_tmp = np.transpose(data_tmp)
        data_tmp = np.diff(data_tmp)
        data_tmp = abs(data_tmp)
        # data_tmp = np.array(data_tmp)
        data_tmp = data_tmp.mean(1)
        if data_timeMean == []:
            data_timeMean = data_tmp
        else:
            data_timeMean = np.row_stack((data_timeMean, data_tmp))

    # 计算短时风舞Std值
    data_timeStd = []
    for i in range(0, 7200, 100):
        data_tmp = data[i:i + 100, :]
        data_tmp = np.transpose(data_tmp)
        data_tmp = np.diff(data_tmp)
        data_tmp = data_tmp.std(1)
        if data_timeStd == []:
            data_timeStd = data_tmp
        else:
            data_timeStd = np.row_stack((data_timeStd, data_tmp))

    # 计算短时风舞时间均方根
    data_timeRMS = []
    for i in range(0, 7200, 100):
        data_tmp = data[i:i + 100, :]
        data_tmp = np.transpose(data_tmp)
        data_tmp = np.diff(data_tmp)
        data_tmp = pow(data_tmp, 2)
        data_tmp = data_tmp.mean(1)
        data_tmp = np.sqrt(data_tmp)
        if data_timeRMS == []:
            data_timeRMS = data_tmp
        else:
            data_timeRMS = np.row_stack((data_timeRMS, data_tmp))

    count = 0
    for i in range(1550, 6550, 250):
        data1 = data_timeMax[:, i:i + 1]
        data2 = data_timeMaxMin[:, i:i+1]
        data3 = data_timeMean[:, i:i + 1]
        data4 = data_timeStd[:, i:i + 1]
        data5 = data_timeRMS[:, i:i + 1]
        if count == 0:
            data_3km100 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 1:
            data_3km600 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 2:
            data_4km100 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 3:
            data_4km600 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 4:
            data_5km100 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 5:
            data_5km600 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 6:
            data_6km100 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 7:
            data_6km600 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 8:
            data_7km100 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 9:
            data_7km600 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 10:
            data_8km100 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 11:
            data_8km600 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 12:
            data_9km100 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 13:
            data_9km600 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 14:
            data_10km100 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 15:
            data_10km600 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 16:
            data_11km100 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 17:
            data_11km600 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 18:
            data_12km100 = np.array([data1, data2, data3, data4, data5])
            count = count + 1
            continue
        if count == 19:
            data_12km600 = np.array([data1, data2, data3, data4, data5])
            count = 0
            continue

    print('3.1km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_3.1km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_3.1km.txt')
        data_new_timeMax = np.column_stack((data1, data_3km100[0].reshape(data_3km100.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_3.1km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_3.1km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_3km100[1].reshape(data_3km100.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_3.1km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_3.1km.txt')
        data_new_timeMean = np.column_stack((data1, data_3km100[2].reshape(data_3km100.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_3.1km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_3.1km.txt')
        data_new_timeStd = np.column_stack((data1, data_3km100[3].reshape(data_3km100.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_3.1km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_3.1km.txt')
        data_new_timeRMS = np.column_stack((data1, data_3km100[4].reshape(data_3km100.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_3.1km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_3.1km.txt', data_3km100[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_3.1km.txt', data_3km100[1])
        np.savetxt('timeMean/timeMean_of_Point_at_3.1km.txt', data_3km100[2])
        np.savetxt('timeStd/timeStd_of_Point_at_3.1km.txt', data_3km100[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_3.1km.txt', data_3km100[4])

    print('3.6km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_3.6km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_3.6km.txt')
        data_new_timeMax = np.column_stack((data1, data_3km600[0].reshape(data_3km600.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_3.6km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_3.6km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_3km600[1].reshape(data_3km600.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_3.6km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_3.6km.txt')
        data_new_timeMean = np.column_stack((data1, data_3km600[2].reshape(data_3km600.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_3.6km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_3.6km.txt')
        data_new_timeStd = np.column_stack((data1, data_3km600[3].reshape(data_3km600.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_3.6km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_3.6km.txt')
        data_new_timeRMS = np.column_stack((data1, data_3km600[4].reshape(data_3km600.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_3.6km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_3.6km.txt', data_3km600[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_3.6km.txt', data_3km600[1])
        np.savetxt('timeMean/timeMean_of_Point_at_3.6km.txt', data_3km600[2])
        np.savetxt('timeStd/timeStd_of_Point_at_3.6km.txt', data_3km600[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_3.6km.txt', data_3km600[4])

    print('4.1km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_4.1km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_4.1km.txt')
        data_new_timeMax = np.column_stack((data1, data_4km100[0].reshape(data_4km100.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_4.1km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_4.1km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_4km100[1].reshape(data_4km100.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_4.1km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_4.1km.txt')
        data_new_timeMean = np.column_stack((data1, data_4km100[2].reshape(data_4km100.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_4.1km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_4.1km.txt')
        data_new_timeStd = np.column_stack((data1, data_4km100[3].reshape(data_4km100.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_4.1km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_4.1km.txt')
        data_new_timeRMS = np.column_stack((data1, data_4km100[4].reshape(data_4km100.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_4.1km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_4.1km.txt', data_4km100[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_4.1km.txt', data_4km100[1])
        np.savetxt('timeMean/timeMean_of_Point_at_4.1km.txt', data_4km100[2])
        np.savetxt('timeStd/timeStd_of_Point_at_4.1km.txt', data_4km100[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_4.1km.txt', data_4km100[4])

    print('4.6km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_4.6km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_4.6km.txt')
        data_new_timeMax = np.column_stack((data1, data_4km600[0].reshape(data_4km600.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_4.6km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_4.6km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_4km600[1].reshape(data_4km600.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_4.6km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_4.6km.txt')
        data_new_timeMean = np.column_stack((data1, data_4km600[2].reshape(data_4km600.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_4.6km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_4.6km.txt')
        data_new_timeStd = np.column_stack((data1, data_4km600[3].reshape(data_4km600.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_4.6km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_4.6km.txt')
        data_new_timeRMS = np.column_stack((data1, data_4km600[4].reshape(data_4km600.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_4.6km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_4.6km.txt', data_4km600[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_4.6km.txt', data_4km600[1])
        np.savetxt('timeMean/timeMean_of_Point_at_4.6km.txt', data_4km600[2])
        np.savetxt('timeStd/timeStd_of_Point_at_4.6km.txt', data_4km600[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_4.6km.txt', data_4km600[4])

    print('5.1km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_5.1km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_5.1km.txt')
        data_new_timeMax = np.column_stack((data1, data_5km100[0].reshape(data_5km100.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_5.1km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_5.1km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_5km100[1].reshape(data_5km100.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_5.1km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_5.1km.txt')
        data_new_timeMean = np.column_stack((data1, data_5km100[2].reshape(data_5km100.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_5.1km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_5.1km.txt')
        data_new_timeStd = np.column_stack((data1, data_5km100[3].reshape(data_5km100.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_5.1km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_5.1km.txt')
        data_new_timeRMS = np.column_stack((data1, data_5km100[4].reshape(data_5km100.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_5.1km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_5.1km.txt', data_5km100[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_5.1km.txt', data_5km100[1])
        np.savetxt('timeMean/timeMean_of_Point_at_5.1km.txt', data_5km100[2])
        np.savetxt('timeStd/timeStd_of_Point_at_5.1km.txt', data_5km100[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_5.1km.txt', data_5km100[4])

    print('5.6km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_5.6km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_5.6km.txt')
        data_new_timeMax = np.column_stack((data1, data_5km600[0].reshape(data_5km600.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_5.6km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_5.6km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_5km600[1].reshape(data_5km600.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_5.6km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_5.6km.txt')
        data_new_timeMean = np.column_stack((data1, data_5km600[2].reshape(data_5km600.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_5.6km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_5.6km.txt')
        data_new_timeStd = np.column_stack((data1, data_5km600[3].reshape(data_5km600.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_5.6km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_5.6km.txt')
        data_new_timeRMS = np.column_stack((data1, data_5km600[4].reshape(data_5km600.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_5.6km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_5.6km.txt', data_5km600[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_5.6km.txt', data_5km600[1])
        np.savetxt('timeMean/timeMean_of_Point_at_5.6km.txt', data_5km600[2])
        np.savetxt('timeStd/timeStd_of_Point_at_5.6km.txt', data_5km600[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_5.6km.txt', data_5km600[4])

    print('6.1km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_6.1km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_6.1km.txt')
        data_new_timeMax = np.column_stack((data1, data_6km100[0].reshape(data_6km100.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_6.1km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_6.1km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_6km100[1].reshape(data_6km100.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_6.1km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_6.1km.txt')
        data_new_timeMean = np.column_stack((data1, data_6km100[2].reshape(data_6km100.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_6.1km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_6.1km.txt')
        data_new_timeStd = np.column_stack((data1, data_6km100[3].reshape(data_6km100.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_6.1km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_6.1km.txt')
        data_new_timeRMS = np.column_stack((data1, data_6km100[4].reshape(data_6km100.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_6.1km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_6.1km.txt', data_6km100[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_6.1km.txt', data_6km100[1])
        np.savetxt('timeMean/timeMean_of_Point_at_6.1km.txt', data_6km100[2])
        np.savetxt('timeStd/timeStd_of_Point_at_6.1km.txt', data_6km100[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_6.1km.txt', data_6km100[4])

    print('6.6km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_6.6km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_6.6km.txt')
        data_new_timeMax = np.column_stack((data1, data_6km600[0].reshape(data_6km600.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_6.6km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_6.6km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_6km600[1].reshape(data_6km600.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_6.6km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_6.6km.txt')
        data_new_timeMean = np.column_stack((data1, data_6km600[2].reshape(data_6km600.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_6.6km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_6.6km.txt')
        data_new_timeStd = np.column_stack((data1, data_6km600[3].reshape(data_6km600.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_6.6km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_6.6km.txt')
        data_new_timeRMS = np.column_stack((data1, data_6km600[4].reshape(data_6km600.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_6.6km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_6.6km.txt', data_6km600[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_6.6km.txt', data_6km600[1])
        np.savetxt('timeMean/timeMean_of_Point_at_6.6km.txt', data_6km600[2])
        np.savetxt('timeStd/timeStd_of_Point_at_6.6km.txt', data_6km600[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_6.6km.txt', data_6km600[4])

    print('7.1km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_7.1km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_7.1km.txt')
        data_new_timeMax = np.column_stack((data1, data_7km100[0].reshape(data_7km100.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_7.1km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_7.1km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_7km100[1].reshape(data_7km100.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_7.1km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_7.1km.txt')
        data_new_timeMean = np.column_stack((data1, data_7km100[2].reshape(data_7km100.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_7.1km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_7.1km.txt')
        data_new_timeStd = np.column_stack((data1, data_7km100[3].reshape(data_7km100.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_7.1km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_7.1km.txt')
        data_new_timeRMS = np.column_stack((data1, data_7km100[4].reshape(data_7km100.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_7.1km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_7.1km.txt', data_7km100[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_7.1km.txt', data_7km100[1])
        np.savetxt('timeMean/timeMean_of_Point_at_7.1km.txt', data_7km100[2])
        np.savetxt('timeStd/timeStd_of_Point_at_7.1km.txt', data_7km100[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_7.1km.txt', data_7km100[4])

    print('7.6km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_7.6km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_7.6km.txt')
        data_new_timeMax = np.column_stack((data1, data_7km600[0].reshape(data_7km600.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_7.6km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_7.6km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_7km600[1].reshape(data_7km600.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_7.6km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_7.6km.txt')
        data_new_timeMean = np.column_stack((data1, data_7km600[2].reshape(data_7km600.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_7.6km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_7.6km.txt')
        data_new_timeStd = np.column_stack((data1, data_7km600[3].reshape(data_7km600.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_7.6km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_7.6km.txt')
        data_new_timeRMS = np.column_stack((data1, data_7km600[4].reshape(data_7km600.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_7.6km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_7.6km.txt', data_7km600[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_7.6km.txt', data_7km600[1])
        np.savetxt('timeMean/timeMean_of_Point_at_7.6km.txt', data_7km600[2])
        np.savetxt('timeStd/timeStd_of_Point_at_7.6km.txt', data_7km600[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_7.6km.txt', data_7km600[4])

    print('8.1km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_8.1km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_8.1km.txt')
        data_new_timeMax = np.column_stack((data1, data_8km100[0].reshape(data_8km100.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_8.1km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_8.1km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_8km100[1].reshape(data_8km100.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_8.1km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_8.1km.txt')
        data_new_timeMean = np.column_stack((data1, data_8km100[2].reshape(data_8km100.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_8.1km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_8.1km.txt')
        data_new_timeStd = np.column_stack((data1, data_8km100[3].reshape(data_8km100.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_8.1km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_8.1km.txt')
        data_new_timeRMS = np.column_stack((data1, data_8km100[4].reshape(data_8km100.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_8.1km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_8.1km.txt', data_8km100[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_8.1km.txt', data_8km100[1])
        np.savetxt('timeMean/timeMean_of_Point_at_8.1km.txt', data_8km100[2])
        np.savetxt('timeStd/timeStd_of_Point_at_8.1km.txt', data_8km100[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_8.1km.txt', data_8km100[4])

    print('8.6km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_8.6km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_8.6km.txt')
        data_new_timeMax = np.column_stack((data1, data_8km600[0].reshape(data_8km600.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_8.6km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_8.6km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_8km600[1].reshape(data_8km600.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_8.6km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_8.6km.txt')
        data_new_timeMean = np.column_stack((data1, data_8km600[2].reshape(data_8km600.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_8.6km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_8.6km.txt')
        data_new_timeStd = np.column_stack((data1, data_8km600[3].reshape(data_8km600.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_8.6km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_8.6km.txt')
        data_new_timeRMS = np.column_stack((data1, data_8km600[4].reshape(data_8km600.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_8.6km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_8.6km.txt', data_8km600[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_8.6km.txt', data_8km600[1])
        np.savetxt('timeMean/timeMean_of_Point_at_8.6km.txt', data_8km600[2])
        np.savetxt('timeStd/timeStd_of_Point_at_8.6km.txt', data_8km600[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_8.6km.txt', data_8km600[4])

    print('9.1km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_9.1km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_9.1km.txt')
        data_new_timeMax = np.column_stack((data1, data_9km100[0].reshape(data_9km100.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_9.1km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_9.1km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_9km100[1].reshape(data_9km100.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_9.1km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_9.1km.txt')
        data_new_timeMean = np.column_stack((data1, data_9km100[2].reshape(data_9km100.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_9.1km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_9.1km.txt')
        data_new_timeStd = np.column_stack((data1, data_9km100[3].reshape(data_9km100.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_9.1km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_9.1km.txt')
        data_new_timeRMS = np.column_stack((data1, data_9km100[4].reshape(data_9km100.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_9.1km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_9.1km.txt', data_9km100[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_9.1km.txt', data_9km100[1])
        np.savetxt('timeMean/timeMean_of_Point_at_9.1km.txt', data_9km100[2])
        np.savetxt('timeStd/timeStd_of_Point_at_9.1km.txt', data_9km100[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_9.1km.txt', data_9km100[4])

    print('9.6km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_9.6km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_9.6km.txt')
        data_new_timeMax = np.column_stack((data1, data_9km600[0].reshape(data_9km600.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_9.6km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_9.6km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_9km600[1].reshape(data_9km600.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_9.6km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_9.6km.txt')
        data_new_timeMean = np.column_stack((data1, data_9km600[2].reshape(data_9km600.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_9.6km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_9.6km.txt')
        data_new_timeStd = np.column_stack((data1, data_9km600[3].reshape(data_9km600.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_9.6km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_9.6km.txt')
        data_new_timeRMS = np.column_stack((data1, data_9km600[4].reshape(data_9km600.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_9.6km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_9.6km.txt', data_9km600[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_9.6km.txt', data_9km600[1])
        np.savetxt('timeMean/timeMean_of_Point_at_9.6km.txt', data_9km600[2])
        np.savetxt('timeStd/timeStd_of_Point_at_9.6km.txt', data_9km600[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_9.6km.txt', data_9km600[4])

    print('10.1km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_10.1km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_10.1km.txt')
        data_new_timeMax = np.column_stack((data1, data_10km100[0].reshape(data_10km100.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_10.1km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_10.1km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_10km100[1].reshape(data_10km100.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_10.1km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_10.1km.txt')
        data_new_timeMean = np.column_stack((data1, data_10km100[2].reshape(data_10km100.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_10.1km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_10.1km.txt')
        data_new_timeStd = np.column_stack((data1, data_10km100[3].reshape(data_10km100.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_10.1km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_10.1km.txt')
        data_new_timeRMS = np.column_stack((data1, data_10km100[4].reshape(data_10km100.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_10.1km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_10.1km.txt', data_10km100[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_10.1km.txt', data_10km100[1])
        np.savetxt('timeMean/timeMean_of_Point_at_10.1km.txt', data_10km100[2])
        np.savetxt('timeStd/timeStd_of_Point_at_10.1km.txt', data_10km100[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_10.1km.txt', data_10km100[4])

    print('10.6km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_10.6km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_10.6km.txt')
        data_new_timeMax = np.column_stack((data1, data_10km600[0].reshape(data_10km600.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_10.6km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_10.6km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_10km600[1].reshape(data_10km600.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_10.6km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_10.6km.txt')
        data_new_timeMean = np.column_stack((data1, data_10km600[2].reshape(data_10km600.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_10.6km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_10.6km.txt')
        data_new_timeStd = np.column_stack((data1, data_10km600[3].reshape(data_10km600.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_10.6km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_10.6km.txt')
        data_new_timeRMS = np.column_stack((data1, data_10km600[4].reshape(data_10km600.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_10.6km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_10.6km.txt', data_10km600[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_10.6km.txt', data_10km600[1])
        np.savetxt('timeMean/timeMean_of_Point_at_10.6km.txt', data_10km600[2])
        np.savetxt('timeStd/timeStd_of_Point_at_10.6km.txt', data_10km600[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_10.6km.txt', data_10km600[4])

    print('11.1km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_11.1km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_11.1km.txt')
        data_new_timeMax = np.column_stack((data1, data_11km100[0].reshape(data_11km100.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_11.1km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_11.1km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_11km100[1].reshape(data_11km100.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_11.1km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_11.1km.txt')
        data_new_timeMean = np.column_stack((data1, data_11km100[2].reshape(data_11km100.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_11.1km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_11.1km.txt')
        data_new_timeStd = np.column_stack((data1, data_11km100[3].reshape(data_11km100.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_11.1km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_11.1km.txt')
        data_new_timeRMS = np.column_stack((data1, data_11km100[4].reshape(data_11km100.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_11.1km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_11.1km.txt', data_11km100[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_11.1km.txt', data_11km100[1])
        np.savetxt('timeMean/timeMean_of_Point_at_11.1km.txt', data_11km100[2])
        np.savetxt('timeStd/timeStd_of_Point_at_11.1km.txt', data_11km100[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_11.1km.txt', data_11km100[4])

    print('11.6km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_11.6km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_11.6km.txt')
        data_new_timeMax = np.column_stack((data1, data_11km600[0].reshape(data_11km600.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_11.6km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_11.6km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_11km600[1].reshape(data_11km600.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_11.6km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_11.6km.txt')
        data_new_timeMean = np.column_stack((data1, data_11km600[2].reshape(data_11km600.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_11.6km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_11.6km.txt')
        data_new_timeStd = np.column_stack((data1, data_11km600[3].reshape(data_11km600.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_11.6km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_11.6km.txt')
        data_new_timeRMS = np.column_stack((data1, data_11km600[4].reshape(data_11km600.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_11.6km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_11.6km.txt', data_11km600[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_11.6km.txt', data_11km600[1])
        np.savetxt('timeMean/timeMean_of_Point_at_11.6km.txt', data_11km600[2])
        np.savetxt('timeStd/timeStd_of_Point_at_11.6km.txt', data_11km600[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_11.6km.txt', data_11km600[4])

    print('12.1km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_12.1km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_12.1km.txt')
        data_new_timeMax = np.column_stack((data1, data_12km100[0].reshape(data_12km100.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_12.1km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_12.1km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_12km100[1].reshape(data_12km100.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_12.1km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_12.1km.txt')
        data_new_timeMean = np.column_stack((data1, data_12km100[2].reshape(data_12km100.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_12.1km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_12.1km.txt')
        data_new_timeStd = np.column_stack((data1, data_12km100[3].reshape(data_12km100.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_12.1km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_12.1km.txt')
        data_new_timeRMS = np.column_stack((data1, data_12km100[4].reshape(data_12km100.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_12.1km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_12.1km.txt', data_12km100[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_12.1km.txt', data_12km100[1])
        np.savetxt('timeMean/timeMean_of_Point_at_12.1km.txt', data_12km100[2])
        np.savetxt('timeStd/timeStd_of_Point_at_12.1km.txt', data_12km100[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_12.1km.txt', data_12km100[4])

    print('12.6km:')
    if os.path.exists('timeMax/timeMax_of_Point_at_12.6km.txt'):
        data1 = np.genfromtxt('timeMax/timeMax_of_Point_at_12.6km.txt')
        data_new_timeMax = np.column_stack((data1, data_12km600[0].reshape(data_12km600.shape[1], )))
        print(data_new_timeMax.shape)
        np.savetxt('timeMax/timeMax_of_Point_at_12.6km.txt', data_new_timeMax)

        data1 = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_12.6km.txt')
        data_new_timeMaxMin = np.column_stack((data1, data_12km600[1].reshape(data_12km600.shape[1], )))
        print(data_new_timeMaxMin.shape)
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_12.6km.txt', data_new_timeMaxMin)

        data1 = np.genfromtxt('timeMean/timeMean_of_Point_at_12.6km.txt')
        data_new_timeMean = np.column_stack((data1, data_12km600[2].reshape(data_12km600.shape[1], )))
        print(data_new_timeMean.shape)
        np.savetxt('timeMean/timeMean_of_Point_at_12.6km.txt', data_new_timeMean)

        data1 = np.genfromtxt('timeStd/timeStd_of_Point_at_12.6km.txt')
        data_new_timeStd = np.column_stack((data1, data_12km600[3].reshape(data_12km600.shape[1], )))
        print(data_new_timeStd.shape)
        np.savetxt('timeStd/timeStd_of_Point_at_12.6km.txt', data_new_timeStd)

        data1 = np.genfromtxt('timeRMS/timeRMS_of_Point_at_12.6km.txt')
        data_new_timeRMS = np.column_stack((data1, data_12km600[4].reshape(data_12km600.shape[1], )))
        print(data_new_timeRMS.shape)
        np.savetxt('timeRMS/timeRMS_of_Point_at_12.6km.txt', data_new_timeRMS)
    else:
        np.savetxt('timeMax/timeMax_of_Point_at_12.6km.txt', data_12km600[0])
        np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_12.6km.txt', data_12km600[1])
        np.savetxt('timeMean/timeMean_of_Point_at_12.6km.txt', data_12km600[2])
        np.savetxt('timeStd/timeStd_of_Point_at_12.6km.txt', data_12km600[3])
        np.savetxt('timeRMS/timeRMS_of_Point_at_12.6km.txt', data_12km600[4])
