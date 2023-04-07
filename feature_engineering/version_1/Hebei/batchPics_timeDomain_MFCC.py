# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from travel_txt_demo import travel_txt, list_files
from librosa.feature import spectral

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

    # 计算梅尔倒谱系数
    mfcc = spectral.mfcc(data, sr=fs, n_mfcc=16)

    # 绘图
    pl.subplot(441)
    pl.plot(mfcc[0, :], color='orange')

    pl.subplot(442)
    pl.plot(mfcc[1, :], color='orange')
    pl.title(u"MFCC (16 Coefficients) of ")

    pl.subplot(443)
    pl.plot(mfcc[2, :], color='orange')
    pl.title(u"Diff Data of Point at" + SpacePoint)

    pl.subplot(444)
    pl.plot(mfcc[3, :], color='orange')

    pl.subplot(445)
    pl.plot(mfcc[4, :], color='orange')

    pl.subplot(446)
    pl.plot(mfcc[5, :], color='orange')

    pl.subplot(447)
    pl.plot(mfcc[6, :], color='orange')

    pl.subplot(448)
    pl.plot(mfcc[7, :], color='orange')

    pl.subplot(449)
    pl.plot(mfcc[8, :], color='orange')

    pl.subplot(4, 4, 10)
    pl.plot(mfcc[9, :], color='orange')

    pl.subplot(4, 4, 11)
    pl.plot(mfcc[10, :], color='orange')

    pl.subplot(4, 4, 12)
    pl.plot(mfcc[11, :], color='orange')

    pl.subplot(4, 4, 13)
    pl.plot(mfcc[12, :], color='orange')

    pl.subplot(4, 4, 14)
    pl.plot(mfcc[13, :], color='orange')

    pl.subplot(4, 4, 15)
    pl.plot(mfcc[14, :], color='orange')

    pl.subplot(4, 4, 16)
    pl.plot(mfcc[15, :], color='orange')

    pl.subplots_adjust(hspace=0.6)
    pl.savefig(u"batchPics/timeDomain/mfcc/MFCC of Diff Data of Point at " + SpacePoint + u".jpg")
