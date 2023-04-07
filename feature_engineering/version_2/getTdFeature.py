# -*- coding: utf-8 -*-
from sklearn.preprocessing import PolynomialFeatures
from travel_path import *

path_timeMax = "timeMax/"
path_timeMaxMin = "timeMaxMin/"
path_timeMean = "timeMean/"
path_timeStd = "timeStd/"
path_timeRMS = "timeRMS/"

files_timeMax = travel_txt(path_timeMax)
files_timeMaxMin = travel_txt(path_timeMaxMin)
files_timeMean = travel_txt(path_timeMean)
files_timeStd = travel_txt(path_timeStd)
files_timeRMS = travel_txt(path_timeRMS)

for i in range(20):

    SpacePoint = ""
    if i == 0:
        SpacePoint = "10.1km"
    elif i == 1:
        SpacePoint = "10.6km"
    elif i == 2:
        SpacePoint = "11.1km"
    elif i == 3:
        SpacePoint = "11.6km"
    elif i == 4:
        SpacePoint = "12.1km"
    elif i == 5:
        SpacePoint = "12.6km"
    elif i == 6:
        SpacePoint = "3.1km"
    elif i == 7:
        SpacePoint = "3.6km"
    elif i == 8:
        SpacePoint = "4.1km"
    elif i == 9:
        SpacePoint = "4.6km"
    elif i == 10:
        SpacePoint = "5.1km"
    elif i == 11:
        SpacePoint = "5.6km"
    elif i == 12:
        SpacePoint = "6.1km"
    elif i == 13:
        SpacePoint = "6.6km"
    elif i == 14:
        SpacePoint = "7.1km"
    elif i == 15:
        SpacePoint = "7.6km"
    elif i == 16:
        SpacePoint = "8.1km"
    elif i == 17:
        SpacePoint = "8.6km"
    elif i == 18:
        SpacePoint = "9.1km"
    else:
        SpacePoint = "9.6km"

    poly4 = PolynomialFeatures(4)

    # 获取风舞差分信号timeMax
    data_timeMax = np.genfromtxt(files_timeMax[i])
    data_timeMax = np.array(data_timeMax)
    data_timeMax = np.transpose(data_timeMax)
    data_timeMax = data_timeMax.reshape(72 * 24)

    # Normalization
    max_tmax = np.max(data_timeMax)
    data_timeMax = data_timeMax / np.float64(max_tmax)
    mean_max = np.mean(data_timeMax)
    data_timeMax = data_timeMax - mean_max
    data_timeMax = np.abs(data_timeMax)

    t_timeMax = np.arange(0, 24, 24.0 / (72 * 24))

    # 获取风舞差分信号timeMaxMin
    data_timeMaxMin = np.genfromtxt(files_timeMaxMin[i])
    data_timeMaxMin = np.array(data_timeMaxMin)
    data_timeMaxMin = np.transpose(data_timeMaxMin)
    data_timeMaxMin = data_timeMaxMin.reshape(72 * 24)

    # Normalization
    max_tmaxmin = np.max(data_timeMaxMin)
    data_timeMaxMin = data_timeMaxMin / np.float64(max_tmaxmin)
    mean_maxmin = np.mean(data_timeMaxMin)
    data_timeMaxMin = data_timeMaxMin - mean_maxmin
    data_timeMaxMin = np.abs(data_timeMaxMin)

    t_timeMaxMin = np.arange(0, 24, 24.0 / (72 * 24))

    # 获取风舞差分信号timeMean
    data_timeMean = np.genfromtxt(files_timeMean[i])
    data_timeMean = np.array(data_timeMean)
    data_timeMean = np.transpose(data_timeMean)
    data_timeMean = data_timeMean.reshape(72 * 24)

    # Normalization
    max_tmean = np.max(data_timeMean)
    data_timeMean = data_timeMean / np.float64(max_tmean)
    mean_mean = np.mean(data_timeMean)
    data_timeMean = data_timeMean - mean_mean
    data_timeMean = np.abs(data_timeMean)

    t_timeMean = np.arange(0, 24, 24.0 / (72 * 24))

    # 获取风舞差分信号timeStd
    data_timeStd = np.genfromtxt(files_timeStd[i])
    data_timeStd = np.array(data_timeStd)
    data_timeStd = np.transpose(data_timeStd)
    data_timeStd = data_timeStd.reshape(72 * 24)

    # Normalization
    max_tstd = np.max(data_timeStd)
    data_timeStd = data_timeStd / np.float64(max_tstd)
    mean_std = np.mean(data_timeStd)
    data_timeStd = data_timeStd - mean_std
    data_timeStd = np.abs(data_timeStd)

    t_timeStd = np.arange(0, 24, 24.0 / (72 * 24))

    # 获取风舞差分信号timeRMS
    data_timeRMS = np.genfromtxt(files_timeRMS[i])
    data_timeRMS = np.array(data_timeRMS)
    data_timeRMS = np.transpose(data_timeRMS)
    data_timeRMS = data_timeRMS.reshape(72 * 24)

    # Normalization
    max_trms = np.max(data_timeRMS)
    data_timeRMS = data_timeRMS / np.float64(max_trms)
    mean_rms = np.mean(data_timeRMS)
    data_timeRMS = data_timeRMS - mean_rms
    data_timeRMS = np.abs(data_timeRMS)

    t_timeRMS = np.arange(0, 24, 24.0 / (72 * 24))

    data_new = data_timeMax
    data_new = np.row_stack((data_new, data_timeMaxMin))
    data_new = np.row_stack((data_new, data_timeMean))
    data_new = np.row_stack((data_new, data_timeStd))
    data_new = np.row_stack((data_new, data_timeRMS))
    data_new = data_new*255.0

    t_new = np.arange(0, 24.0, 24.0/ (72*24))

    np.savetxt(u"features/timeDomain/compound/noPoly/Compound-Features of Point at " + SpacePoint + u".txt", data_new)
