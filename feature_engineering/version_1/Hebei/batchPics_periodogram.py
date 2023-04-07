# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from scikits.talkbox.spectral import basic
from travel_txt_demo import travel_txt, list_files

path_original = "SpacePoint/"
files_original = travel_txt(path_original)
print "遍历文件夹files_original得到如下文件："
list_files(files_original)

pl.figure(figsize=(16, 11))

for i in xrange(10):

    SpacePoint = ""
    count = 0
    if i == 0:
        SpacePoint = "0.1km"
        count = 1
    elif i == 1:
        SpacePoint = "12.1km"
        count = 5
    elif i == 2:
        SpacePoint = "15.1km"
        count = 6
    elif i == 3:
        SpacePoint = "18.1km"
        count = 7
    elif i == 4:
        SpacePoint = "21.1km"
        count = 8
    elif i == 5:
        SpacePoint = "24.1km"
        count = 9
    elif i == 6:
        SpacePoint = "27.1km"
        count = 10
    elif i == 7:
        SpacePoint = "3.1km"
        count = 2
    elif i == 8:
        SpacePoint = "timeSeg"
        count = 3
    else:
        SpacePoint = "9.1km"
        count = 4

    # 获取原始风舞信号和风舞差分信号
    data = np.genfromtxt(files_original[i])
    data = np.array(data)
    data_o = data
    data = np.diff(data)

    fs = data.shape[0]
    fs = fs / (24 * 3600.0)

    data_periodogram = basic.periodogram(data, fs=fs)

    pl.subplot(5, 2, count)
    pl.plot(data_periodogram)
    pl.xlabel(u"Frequency / Hz")
    pl.ylabel(u"Amplitude / V")
    pl.title('Periodogram of Diff Data of Point at' + SpacePoint)
    pl.tight_layout()

pl.subplots_adjust(hspace=0.6)
pl.savefig(u"batchPics/Periodogram.jpg")
