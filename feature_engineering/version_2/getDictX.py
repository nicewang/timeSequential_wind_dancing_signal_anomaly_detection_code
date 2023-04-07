import numpy as np
import pylab as pl

data_max = np.genfromtxt('timeMax/timeMax_of_Point_at_0.1km.txt')
data_max = data_max.reshape(72 * 24, )
# Normalization
max_tmax = np.max(data_max)
data_max = data_max / np.float64(max_tmax)
mean_max = np.mean(data_max)
data_max = data_max - mean_max + 1
pl.plot(data_max)
pl.show()

data_maxmin = np.genfromtxt('timeMaxMin/timeMaxMin_of_Point_at_0.1km.txt')
data_maxmin = data_maxmin.reshape(72 * 24, )
# Normalization
max_tmaxmin = np.max(data_maxmin)
data_maxmin = data_maxmin / np.float64(max_tmaxmin)
mean_maxmin = np.mean(data_maxmin)
data_maxmin = data_maxmin - mean_maxmin + 1
pl.plot(data_maxmin)
pl.show()

data_mean = np.genfromtxt('timeMean/timeMean_of_Point_at_0.1km.txt')
data_mean = data_mean.reshape(72 * 24, )
# Normalization
max_tmean = np.max(data_mean)
data_mean = data_mean / np.float64(max_tmean)
mean_mean = np.mean(data_mean)
data_mean = data_mean - mean_mean + 1
pl.plot(data_mean)
pl.show()

data_std = np.genfromtxt('timeStd/timeStd_of_Point_at_0.1km.txt')
data_std = data_std.reshape(72 * 24, )
# Normalization
max_tstd = np.max(data_std)
data_std = data_std / np.float64(max_tstd)
mean_std = np.mean(data_std)
data_std = data_std - mean_std + 1
pl.plot(data_std)
pl.show()

data_rms = np.genfromtxt('timeRMS/timeRMS_of_Point_at_0.1km.txt')
data_rms = data_rms.reshape(72 * 24, )
# Normalization
max_trms = np.max(data_rms)
data_rms = data_rms / np.float64(max_trms)
mean_rms = np.mean(data_rms)
data_rms = data_rms - mean_rms + 1
pl.plot(data_rms)
pl.show()

data_chroma = np.genfromtxt('chromaFeature/100len/ChromaFeature of Point at 0.1km.txt')

labels = np.genfromtxt('labels/labels of point at 0.1km.txt')

# df = []
data_out = []
for i in range(1728):
    data = np.array((data_max[i] * data_chroma[:, i], data_maxmin[i] * data_chroma[:, i], data_mean[i] * data_chroma[:, i],
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

np.savetxt(u'labeledFeature/Labeled Feature of Point at 0.1km.txt', data_out)