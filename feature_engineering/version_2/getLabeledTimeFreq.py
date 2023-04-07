# -*- coding: utf-8 -*-
from travel_path import *

data_path = "original_onePointData/"
label_path = 'labels-0.55/mild_outliers/'

data_files = travel_txt(data_path)
label_files = travel_txt(label_path)

path_max = 'timeMax/'
path_maxmin = 'timeMaxMin/'
path_mean = 'timeMean/'
path_std = 'timeStd/'
path_rms = 'timeRMS/'
path_chroma = 'chromaFeature/100len/'
path_label = 'labels-0.55/mild_outliers/'

file_max = travel_txt(path_max)
file_maxmin = travel_txt(path_maxmin)
file_mean = travel_txt(path_mean)
file_std = travel_txt(path_std)
file_rms = travel_txt(path_rms)
file_chroma = travel_txt(path_chroma)
file_labels = travel_txt(path_label)

for i in range(data_files.shape[0]):

    SpacePoint = data_files[i].split('_')[-1]
    SpacePoint1 = label_files[i].split(' ')[-1]

    if SpacePoint == SpacePoint1:
        print('Bingo!',SpacePoint)

    data = np.genfromtxt(data_files[i])
    data = np.array(data)
    data = np.diff(data)

    label = np.genfromtxt(label_files[i])

    data_max = np.genfromtxt(file_max[i])
    if i > 0:
        data_max = np.transpose(data_max)
    data_max = data_max.reshape(72 * 24, )
    # Normalization
    max_tmax = np.max(data_max)
    data_max = data_max / np.float64(max_tmax)
    mean_max = np.mean(data_max)
    data_max = data_max - mean_max + 1

    data_maxmin = np.genfromtxt(file_maxmin[i])
    if i > 0:
        data_maxmin = np.transpose(data_maxmin)
    data_maxmin = data_maxmin.reshape(72 * 24, )
    # Normalization
    max_tmaxmin = np.max(data_maxmin)
    data_maxmin = data_maxmin / np.float64(max_tmaxmin)
    mean_maxmin = np.mean(data_maxmin)
    data_maxmin = data_maxmin - mean_maxmin + 1

    data_mean = np.genfromtxt(file_mean[i])
    if i > 0:
        data_mean = np.transpose(data_mean)
    data_mean = data_mean.reshape(72 * 24, )
    # Normalization
    max_tmean = np.max(data_mean)
    data_mean = data_mean / np.float64(max_tmean)
    mean_mean = np.mean(data_mean)
    data_mean = data_mean - mean_mean + 1

    data_std = np.genfromtxt(file_std[i])
    if i > 0:
        data_std = np.transpose(data_std)
    data_std = data_std.reshape(72 * 24, )
    # Normalization
    max_tstd = np.max(data_std)
    data_std = data_std / np.float64(max_tstd)
    mean_std = np.mean(data_std)
    data_std = data_std - mean_std + 1

    data_rms = np.genfromtxt(file_rms[i])
    if i > 0:
        data_rms = np.transpose(data_rms)
    data_rms = data_rms.reshape(72 * 24, )
    # Normalization
    max_trms = np.max(data_rms)
    data_rms = data_rms / np.float64(max_trms)
    mean_rms = np.mean(data_rms)
    data_rms = data_rms - mean_rms + 1

    data_out = []
    for j in range(1728):
        if j == 1727:
            sub_data = data[100*j-8:100*(j+1)]
        else:
            sub_data = data[100*j:100*(j+1)]
        # 进行快速傅立叶变换
        xf = np.fft.rfft(sub_data)
        xf = np.abs(xf)
        xf = xf / max(xf)
        xf = xf[:50]
        # print(xf.shape)
        label_tmp = label[j]
        data_tmp = np.array(
            (data_max[j] * xf, data_maxmin[j] * xf, data_mean[j] * xf,
             data_std[j] * xf, data_rms[j] * xf))
        data_tmp = data_tmp.reshape(250, 1)
        data_tmp = np.row_stack((data_tmp, label[j]))
        data_tmp = data_tmp.reshape(251, )
        if j == 0:
            data_out = data_tmp
        else:
            data_out = np.column_stack((data_out, data_tmp))

    print(data_out.shape)
    np.savetxt(u'labeledTimeFreq/Labeled Freq Feature of Point at ' + SpacePoint, data_out)

# np.savetxt('freq_models/freq model1 of 3.1km-1132.txt',xf)