# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from librosa.feature import spectral
from travel_txt_demo import travel_txt, list_files

path_original = "SpacePoint/"
files_original = travel_txt(path_original)
print "遍历文件夹files_original得到如下文件："
list_files(files_original)

for i in xrange(10):

    SpacePoint = ""
    if i == 0:
        SpacePoint = "0.1km"
    elif i == 1:
        SpacePoint = "12.1km"
    elif i == 2:
        SpacePoint = "15.1km"
    elif i == 3:
        SpacePoint = "18.1km"
    elif i == 4:
        SpacePoint = "21.1km"
    elif i == 5:
        SpacePoint = "24.1km"
    elif i == 6:
        SpacePoint = "27.1km"
    elif i == 7:
        SpacePoint = "3.1km"
    elif i == 8:
        SpacePoint = "timeSeg"
    else:
        SpacePoint = "9.1km"

    pl.figure(figsize=(16,3.8))

    # 获取原始风舞信号和风舞差分信号
    data = np.genfromtxt(files_original[i])
    data = np.array(data)
    data_o = data
    data = np.diff(data)

    fs = data.shape[0]
    fs = fs / (24 * 3600.0)

    fft_size = data.shape[0]

    t = np.arange(0, 24.0, 24.0 / fft_size)

    # 获取频谱中心和频谱滚降点
    data_spectral_centroid = spectral.spectral_centroid(data, sr=fs)
    data_spectral_centroid = data_spectral_centroid.reshape(
        data_spectral_centroid.shape[0] * data_spectral_centroid.shape[1], )

    t_scentroid = np.arange(0, 24.0, 24.0 / data_spectral_centroid.shape[0])

    data_spectral_rolloff = spectral.spectral_rolloff(data, sr=fs)
    data_spectral_rolloff = data_spectral_rolloff.reshape(
        data_spectral_rolloff.shape[0] * data_spectral_rolloff.shape[1])

    t_srolloff = np.arange(0, 24.0, 24.0 / data_spectral_rolloff.shape[0])

    # 绘制频谱滚降点和频谱中心图
    pl.subplot(121)
    pl.semilogy(t_scentroid, data_spectral_centroid, color='red', label='Spectral centroid')
    pl.ylabel('Frequency / Hz')
    pl.xlabel('Time / h')
    pl.title(u"Spectral Centroid of Diff Data of Point at" + SpacePoint)
    pl.legend()

    pl.subplot(122)
    pl.semilogy(t_srolloff, data_spectral_rolloff, color='brown', label='Roll-off frequency')
    pl.ylabel('Frequency / Hz')
    pl.xlabel('Time / h')
    pl.title(u"Spectral Rolloff of Diff Data of Point at" + SpacePoint)
    pl.legend()

    pl.subplots_adjust(hspace=0.9)
    pl.savefig(u"batchPics/freqDomain/SpectralCentroid_and_SpectralRolloff/Spectral Centroid and Spectral Rolloff of Point at " + SpacePoint + u".jpg")
