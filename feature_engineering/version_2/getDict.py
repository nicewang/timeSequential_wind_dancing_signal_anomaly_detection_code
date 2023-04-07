from travel_path import *
from in2out import *
# import pandas as pd
import pylab as pl

out = in2out(3.1,12.6,0.5)

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

for i in range(1,21):
    SpacePoint = str(out[i-1][0]) + 'km'
    print(SpacePoint)

    data_max = np.genfromtxt(file_max[i])
    data_max = np.transpose(data_max)
    data_max = data_max.reshape(72 * 24, )
    # Normalization
    max_tmax = np.max(data_max)
    data_max = data_max / np.float64(max_tmax)
    mean_max = np.mean(data_max)
    data_max = data_max - mean_max + 1

    data_maxmin = np.genfromtxt(file_maxmin[i])
    data_maxmin = np.transpose(data_maxmin)
    data_maxmin = data_maxmin.reshape(72 * 24, )
    # Normalization
    max_tmaxmin = np.max(data_maxmin)
    data_maxmin = data_maxmin / np.float64(max_tmaxmin)
    mean_maxmin = np.mean(data_maxmin)
    data_maxmin = data_maxmin - mean_maxmin + 1

    data_mean = np.genfromtxt(file_mean[i])
    data_mean = np.transpose(data_mean)
    data_mean = data_mean.reshape(72 * 24, )
    # Normalization
    max_tmean = np.max(data_mean)
    data_mean = data_mean / np.float64(max_tmean)
    mean_mean = np.mean(data_mean)
    data_mean = data_mean - mean_mean + 1

    data_std = np.genfromtxt(file_std[i])
    data_std = np.transpose(data_std)
    data_std = data_std.reshape(72 * 24, )
    # Normalization
    max_tstd = np.max(data_std)
    data_std = data_std / np.float64(max_tstd)
    mean_std = np.mean(data_std)
    data_std = data_std - mean_std + 1

    data_rms = np.genfromtxt(file_rms[i])
    data_rms = np.transpose(data_rms)
    data_rms = data_rms.reshape(72 * 24, )
    # Normalization
    max_trms = np.max(data_rms)
    data_rms = data_rms / np.float64(max_trms)
    mean_rms = np.mean(data_rms)
    data_rms = data_rms - mean_rms + 1

    pl.plot(data_rms)
    pl.show()

    data_chroma = np.genfromtxt(file_chroma[i])

    labels = np.genfromtxt(file_labels[i-1])

    # df = []
    data_out = []
    for i in range(1728):
        data = np.array(
            (data_max[i] * data_chroma[:, i], data_maxmin[i] * data_chroma[:, i], data_mean[i] * data_chroma[:, i],
             data_std[i] * data_chroma[:, i], data_rms[i] * data_chroma[:, i]))
        # print(data)
        data = data.reshape(60, 1)
        data = np.row_stack((data, labels[i]))
        data = data.reshape(61, )
        # data = data.reshape(61, 1)
        # data = data[:60]
        # data = data.reshape(5,12)
        # print(data)

        # if i == 0:
        #     df = pd.DataFrame({i: data})
        # else:
        #     df[i] = data

        if i == 0:
            data_out = data
        else:
            data_out = np.column_stack((data_out, data))

    # print(df)
    # df.to_csv('test.csv')

    np.savetxt(u'labeledFeature-0.55/Labeled Feature of Point at ' + SpacePoint + u'.txt', data_out)
