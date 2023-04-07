# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl

path = "original_onePointData/Data_of_Point_at_9.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data = np.diff(data)

fs = data.shape[0]
fs = fs / (24 * 3600.0)

sampling_rate = fs

# sub_data = data[172700:172800]
# print(sub_data.shape)

# labels = np.genfromtxt('timeStd/labels/extreme_outliers/labels of point at 9.1km.txt')
labels = np.genfromtxt('labels-0.55/mild_outliers/labels of point at 3.1km.txt')

for i in range(labels.shape[0]):
    if labels[i] == 1:
        print(i)
        # 截取信号所在时间段周围10分钟内的所有风舞差分信号
        if i < 6:
            sub_data = data[:1200]
        elif i > 1721:
            sub_data = data[171592:]
        else:
            sub_data = data[100*i-550:100*(i+1)+550]
        # 进行快速傅立叶变换
        xf = np.fft.rfft(sub_data)
        xf = np.abs(xf)
        xf = xf / max(xf)
        freqs = np.linspace(0, sampling_rate / 2,601)
        pl.plot(freqs,xf)
        pl.xlabel(u'Freq / Hz')
        pl.ylabel(u'Amplitude / V')
        pl.show()

# # for checking deleted point
# i = 1042
# sub_data = data[100*i-550:100*(i+1)+550]
# # 进行快速傅立叶变换
# xf = np.fft.rfft(sub_data)
# xf = np.abs(xf)
# xf = xf / max(xf)
# freqs = np.linspace(0, sampling_rate / 2,601)
# pl.plot(freqs,xf)
# pl.xlabel(u'Freq / Hz')
# pl.ylabel(u'Amplitude / V')
# pl.show()
