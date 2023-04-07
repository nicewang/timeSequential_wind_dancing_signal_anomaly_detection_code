# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from pyAudioAnalysis import audioFeatureExtraction
from travel_txt_demo import travel_txt, list_files

path_original = "SpacePoint/"
files_original = travel_txt(path_original)
print "遍历文件夹files_original得到如下文件："
list_files(files_original)

for i in xrange(11):

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
    elif i == 9:
        SpacePoint = "9.1km"
    else:
        SpacePoint = "0.1km"

    pl.figure(figsize=(16,7))

    # 获取原始风舞信号和风舞差分信号
    if(i == 10):
        data = np.genfromtxt(files_original[0])
    else:
        data = np.genfromtxt(files_original[i])
    data = np.array(data)
    data_o = data
    data = np.diff(data)

    fs = data.shape[0]
    fs = fs / (24 * 3600.0)

    sampling_rate = fs
    fft_size = data.shape[0]

    # 计算短时平均能量与短时平均过零率
    F200 = audioFeatureExtraction.stFeatureExtraction(data, 16000, 200, 50)
    zcr200 = np.array(F200[0, :])
    energy200 = np.array(F200[1, :])
    t200 = np.arange(0, 24.0, 24.0 / zcr200.shape[0])

    F1024 = audioFeatureExtraction.stFeatureExtraction(data, 16000, 1024, 256)
    zcr1024 = np.array(F1024[0, :])
    energy1024 = np.array(F1024[1, :])
    t1024 = np.arange(0, 24.0, 24.0 / zcr1024.shape[0])

    F2048 = audioFeatureExtraction.stFeatureExtraction(data, 16000, 2048, 512)
    zcr2048 = np.array(F2048[0, :])
    energy2048 = np.array(F2048[1, :])
    t2048 = np.arange(0, 24.0, 24.0 / zcr2048.shape[0])

    # 绘制短时平均能量与短时平均过零率波形
    pl.subplot(321)
    pl.plot(t200, F200[0, :], color='c', label=u"frame_len=100s,hop_len=25s")
    pl.xlabel(u"Time / h")
    pl.ylabel(u"ZCR")
    pl.title(u"Short Time Average Zero Crossing Rate of Diff Data of Point at" + SpacePoint)
    pl.legend()

    pl.subplot(322)
    pl.plot(t200, F200[1, :], color='m', label=u"frame_len=100s,hop_len=25s")
    pl.xlabel(u"Time / h")
    pl.ylabel(u"Energy")
    pl.title(u"Short Time Average Energy of Diff Data of Point at" + SpacePoint)
    pl.legend()

    pl.subplot(323)
    pl.plot(t1024, F1024[0, :], color='c', label=u"frame_len=512s,hop_len=128s")
    pl.xlabel(u"Time / h")
    pl.ylabel(u"ZCR")
    pl.title(u"Short Time Average Zero Crossing Rate of Diff Data of Point at" + SpacePoint)
    pl.legend()

    pl.subplot(324)
    pl.plot(t1024, F1024[1, :], color='m', label=u"frame_len=512s,hop_len=128s")
    pl.xlabel(u"Time / h")
    pl.ylabel(u"Energy")
    pl.title(u"Short Time Average Energy of Diff Data of Point at" + SpacePoint)
    pl.legend()

    pl.subplot(325)
    pl.plot(t2048, F2048[0, :], color='c', label=u"frame_len=1024s,hop_len=256s")
    pl.xlabel(u"Time / h")
    pl.ylabel(u"ZCR")
    pl.title(u"Short Time Average Zero Crossing Rate of Diff Data of Point at" + SpacePoint)
    pl.legend()

    pl.subplot(326)
    pl.plot(t2048, F2048[1, :], color='m', label=u"frame_len=1024s,hop_len=256s")
    pl.xlabel(u"Time / h")
    pl.ylabel(u"Energy")
    pl.title(u"Short Time Average Energy of Diff Data of Point at" + SpacePoint)
    pl.legend()

    pl.subplots_adjust(hspace=0.6)
    pl.savefig(u"batchPics/timeDomain/ZCRandEnergy/ZCR and Energy Plot of Point at " + SpacePoint + u".jpg")
