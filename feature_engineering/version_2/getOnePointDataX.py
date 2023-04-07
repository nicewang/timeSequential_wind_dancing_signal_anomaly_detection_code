import numpy as np
import pylab as pl

path = 'original_onePointData/Data_of_Point_at_0.1km.txt'
data = np.genfromtxt(path)
data = np.diff(data)

data_timeMax = []
data_timeMaxMin = []
data_timeMean = []
data_timeStd = []
data_timeRMS = []
for i in range(1728):
    data_tmp = data[i*100:(i+1)*100]
    data_abs = abs(data_tmp)

    data_max = data_abs.max(0)
    if data_timeMax == []:
        data_timeMax = data_max
    else:
        data_timeMax = np.row_stack((data_timeMax, data_max))

    max = data_tmp.max(0)
    min = data_tmp.min(0)
    data_maxmin = max - min
    if data_timeMaxMin == []:
        data_timeMaxMin = data_maxmin
    else:
        data_timeMaxMin = np.row_stack((data_timeMaxMin, data_maxmin))

    data_mean = data_abs.mean(0)
    if data_timeMean == []:
        data_timeMean = data_mean
    else:
        data_timeMean = np.row_stack((data_timeMean, data_mean))

    data_std = data_tmp.std(0)
    if data_timeStd == []:
        data_timeStd = data_std
    else:
        data_timeStd = np.row_stack((data_timeStd, data_std))

    data_rms = pow(data_tmp, 2)
    data_rms = data_rms.mean(0)
    data_rms = np.sqrt(data_rms)
    if data_timeRMS == []:
        data_timeRMS = data_rms
    else:
        data_timeRMS = np.row_stack((data_timeRMS, data_rms))

np.savetxt('timeMax/timeMax_of_Point_at_0.1km.txt', data_timeMax)
np.savetxt('timeMaxMin/timeMaxMin_of_Point_at_0.1km.txt', data_timeMaxMin)
np.savetxt('timeMean/timeMean_of_Point_at_0.1km.txt', data_timeMean)
np.savetxt('timeStd/timeStd_of_Point_at_0.1km.txt', data_timeStd)
np.savetxt('timeRMS/timeRMS_of_Point_at_0.1km.txt', data_timeRMS)
