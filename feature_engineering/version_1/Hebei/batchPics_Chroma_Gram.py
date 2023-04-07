# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from librosa.feature import spectral
from travel_txt_demo import travel_txt, list_files
from librosa.display import *

path_original = "SpacePoint/"
files_original = travel_txt(path_original)
print "遍历文件夹files_original得到如下文件："
list_files(files_original)

pl.figure(figsize=(12, 20))

for i in xrange(10):

    # SpacePoint = ""
    # count = 0
    # count_ = 0
    # if i == 0:
    #     SpacePoint = "0.1km"
    #     count = 1
    #     count_ = 3
    # elif i == 1:
    #     SpacePoint = "12.1km"
    #     count = 9
    #     count_ = 11
    # elif i == 2:
    #     SpacePoint = "15.1km"
    #     count = 10
    #     count_ = 12
    # elif i == 3:
    #     SpacePoint = "18.1km"
    #     count = 13
    #     count_ = 15
    # elif i == 4:
    #     SpacePoint = "21.1km"
    #     count = 14
    #     count_ = 16
    # elif i == 5:
    #     SpacePoint = "24.1km"
    #     count = 17
    #     count_ = 19
    # elif i == 6:
    #     SpacePoint = "27.1km"
    #     count = 18
    #     count_ = 20
    # elif i == 7:
    #     SpacePoint = "3.1km"
    #     count = 2
    #     count_ = 4
    # elif i == 8:
    #     SpacePoint = "6.1km"
    #     count = 5
    #     count_ = 7
    # else:
    #     SpacePoint = "9.1km"
    #     count = 6
    #     count_ = 8

    SpacePoint = ""
    count = 0
    count_ = 0
    if i == 0:
        SpacePoint = "0.1km"
        count = 1
        count_ = 1
    elif i == 1:
        SpacePoint = "12.1km"
        count = 9
        count_ = 5
    elif i == 2:
        SpacePoint = "15.1km"
        count = 10
        count_ = 6
    elif i == 3:
        SpacePoint = "18.1km"
        count = 13
        count_ = 7
    elif i == 4:
        SpacePoint = "21.1km"
        count = 14
        count_ = 8
    elif i == 5:
        SpacePoint = "24.1km"
        count = 17
        count_ = 9
    elif i == 6:
        SpacePoint = "27.1km"
        count = 18
        count_ = 10
    elif i == 7:
        SpacePoint = "3.1km"
        count = 2
        count_ = 2
    elif i == 8:
        SpacePoint = "6.1km"
        count = 5
        count_ = 3
    else:
        SpacePoint = "9.1km"
        count = 6
        count_ = 4

    # 获取原始风舞信号和风舞差分信号
    data = np.genfromtxt(files_original[i])
    data = np.array(data)
    data_o = data
    data = np.diff(data)

    t = np.arange(0, 24.0, 24.0 / data.shape[0])

    fs = data.shape[0]
    fs = fs / (24 * 3600.0)

    chroma_gram = spectral.chroma_stft(y=data, sr=fs)

    # pl.subplot(20, 2, count_)
    # specshow(chroma_gram, y_axis='chroma', x_axis='time', hop_length=1536)
    # pl.xlabel(u"Time / h")
    # pl.colorbar()
    # pl.title('Chroma Gram of Diff Data of Point at ' + SpacePoint)
    # pl.tight_layout()
    #
    # pl.subplot(20, 2, count)
    # pl.plot(t, data, color="blue")
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.ylabel(u"Amplitude / V")
    # pl.title(u"Diff Data of Wind Wave of Point at " + SpacePoint)

    pl.subplot(10, 2, count_)
    specshow(chroma_gram, y_axis='chroma', x_axis='time', hop_length=1536)
    pl.xlabel(u"Time / h")
    pl.colorbar()
    pl.title('Chroma Gram of Diff Data of Point at ' + SpacePoint)
    pl.tight_layout()

pl.subplots_adjust(hspace=0.6)
pl.savefig(u"batchPics/Chroma Gram.jpg")
