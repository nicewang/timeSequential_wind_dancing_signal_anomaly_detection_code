# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from travel_txt_demo import travel_txt, list_files
from scipy import fftpack

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

    pl.figure(figsize=(16,5))

    # 获取原始风舞信号和风舞差分信号
    data = np.genfromtxt(files_original[i])
    data = np.array(data)
    data_o = data
    data = np.diff(data)

    fs = data.shape[0]
    fs = fs / (24 * 3600.0)

    sampling_rate = fs
    fft_size = data.shape[0]

    t = np.arange(0, 24.0, 24.0 / fft_size)

    xs = data

    # 进行快速傅立叶变换
    xf = np.fft.rfft(xs)

    freqs = np.linspace(0, sampling_rate / 2, fft_size / 2 + 1)

    # 对风舞差分信号进行希尔伯特变换
    hx = fftpack.hilbert(xs)

    # 对进行希尔伯特变换之后的风舞差分信号再进行快速傅立叶变换
    xfh = np.fft.rfft(hx)

    # 绘制时域波形及频域波形
    pl.subplot(221)
    pl.plot(t, data, color='b',)
    pl.xlabel(u"Time / h")
    pl.ylabel(u"Amplitude / V")
    pl.title(u"Original Diff Data of Point at" + SpacePoint)

    pl.subplot(222)
    pl.plot(t, hx)
    pl.xlabel(u"Time / h")
    pl.ylabel(u"Amplitude / V")
    pl.title(u"Hilbert Transform of Diff Data of Point at" + SpacePoint)

    pl.subplot(223)
    pl.plot(freqs, np.abs(xf), color='b')
    pl.xlabel(u"Frequency / Hz")
    pl.ylabel(u"Amplitude / V")
    pl.title(u"FFT Transform of Diff Data of Point at" + SpacePoint)

    pl.subplot(224)
    pl.plot(freqs, np.abs(xfh))
    pl.xlabel(u"Frequency / Hz")
    pl.ylabel(u"Amplitude / V")
    pl.title(u"Hilbert Spectrum of Diff Data of Point at" + SpacePoint)

    pl.subplots_adjust(hspace=0.6)
    pl.savefig(u"batchPics/freqDomain/Frequency Plot of Point at " + SpacePoint + u".jpg")
