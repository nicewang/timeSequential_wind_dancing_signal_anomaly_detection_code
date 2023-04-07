# -*- coding: utf-8 -*-
import glob
import os
import numpy as np
import pylab as pl

def travel_txt(path):
    cate = [path+x for x in os.listdir(path) if os.path.isdir(path+x)]
    files = []
    for idx,folder in enumerate(cate):
        for im in glob.glob(folder+'/*.txt'):
            print('reading the images:%s'%(im))
            files.append(im)
    return np.asarray(files)

path_original = "SpacePoint/"
path_timeMax = "timeMax/SpacePoint/"
path_timeMaxMin = "timeMaxMin/SpacePoint/"
path_timeMean = "timeMean/SpacePoint/"
path_timeStd = "timeStd/SpacePoint/"
path_timeRMS = "timeRMS/SpacePoint/"

files_original = travel_txt(path_original)
print "遍历文件夹files_original得到如下文件："
for i in xrange(files_original.shape[0]):
    print files_original[i]

files_timeMax = travel_txt(path_timeMax)
print "遍历文件夹files_timeMax得到如下文件："
for i in xrange(files_timeMax.shape[0]):
    print files_timeMax[i]

files_timeMaxMin = travel_txt(path_timeMaxMin)
print "遍历文件夹files_timeMaxMin得到如下文件："
for i in xrange(files_timeMaxMin.shape[0]):
    print files_timeMaxMin[i]

files_timeMean = travel_txt(path_timeMean)
print "遍历文件夹files_timeMean得到如下文件："
for i in xrange(files_timeMean.shape[0]):
    print files_timeMean[i]

files_timeStd = travel_txt(path_timeStd)
print "遍历文件夹files_timeStd得到如下文件："
for i in xrange(files_timeStd.shape[0]):
    print files_timeStd[i]

files_timeRMS = travel_txt(path_timeRMS)
print "遍历文件夹files_timeRMS得到如下文件："
for i in xrange(files_timeRMS.shape[0]):
    print files_timeRMS[i]

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
        SpacePoint = "6.1km"
    else:
        SpacePoint = "9.1km"

    pl.figure(figsize=(16,9))

    # 获取原始风舞信号和风舞差分信号
    data = np.genfromtxt(files_original[i])
    data = np.array(data)
    data_o = data
    data = np.diff(data)

    fs = data.shape[0]
    fs = fs / (24 * 3600.0)

    sampling_rate = fs
    fft_size = data.shape[0]

    t0 = np.arange(0, 24.0, 24.0 / data_o.shape[0])

    t = np.arange(0, 24.0, 24.0 / fft_size)

    # 绘制原始风舞信号波形和风舞差分信号波形
    pl.subplot(421)
    pl.plot(t0, data_o)
    pl.title(u"Original Data of Wind Wave of Point at" + SpacePoint)
    pl.xlabel(u"Time / h")
    pl.ylabel(u"Amplitude / V")

    pl.subplot(422)
    pl.plot(t, data, color="blue")
    pl.title(u"Diff Data of Wind Wave of Point at" + SpacePoint)
    pl.xlabel(u"Time / h")
    pl.ylabel(u"Amplitude / V")

    # 获取风舞差分信号timeMax
    data_timeMax = np.genfromtxt(files_timeMax[i])
    data_timeMax = np.array(data_timeMax)
    data_timeMax = np.transpose(data_timeMax)
    data_timeMax = data_timeMax.reshape(72 * 24)

    t_timeMax = np.arange(0, 24, 24.0 / (72 * 24))

    # 绘制风舞差分信号timeMax波形
    pl.subplot(423)
    pl.plot(t_timeMax, data_timeMax, color='orange')
    pl.xlabel(u"Time / h")
    pl.ylabel(u"TimeMax within 50s / V")
    pl.title(u"TimeMax(within 50s) of Diff Data of Point at" + SpacePoint)

    # 获取风舞差分信号timeMaxMin
    data_timeMaxMin = np.genfromtxt(files_timeMaxMin[i])
    data_timeMaxMin = np.array(data_timeMaxMin)
    data_timeMaxMin = np.transpose(data_timeMaxMin)
    data_timeMaxMin = data_timeMaxMin.reshape(72 * 24)

    t_timeMaxMin = np.arange(0, 24, 24.0 / (72 * 24))

    # 绘制风舞差分信号timeMaxMin波形
    pl.subplot(424)
    pl.plot(t_timeMaxMin, data_timeMaxMin, color='red')
    pl.xlabel(u"Time / h")
    pl.ylabel(u"TimeMaxMin within 50s / V")
    pl.title(u"TimeMaxMin(within 50s) of Diff Data of Point at" + SpacePoint)

    # 获取风舞差分信号timeMean
    data_timeMean = np.genfromtxt(files_timeMean[i])
    data_timeMean = np.array(data_timeMean)
    data_timeMean = np.transpose(data_timeMean)
    data_timeMean = data_timeMean.reshape(72 * 24)

    t_timeMean = np.arange(0, 24, 24.0 / (72 * 24))

    # 绘制风舞差分信号timeMean波形
    pl.subplot(425)
    pl.plot(t_timeMean, data_timeMean, color='purple')
    pl.xlabel(u"Time / h")
    pl.ylabel(u"TimeMean within 50s / V")
    pl.title(u"TimeMean(within 50s) of Diff Data of Point at" + SpacePoint)

    # 获取风舞差分信号timeStd
    data_timeStd = np.genfromtxt(files_timeStd[i])
    data_timeStd = np.array(data_timeStd)
    data_timeStd = np.transpose(data_timeStd)
    data_timeStd = data_timeStd.reshape(72 * 24)

    t_timeStd = np.arange(0, 24, 24.0 / (72 * 24))

    # 绘制风舞差分信号timeStd波形
    pl.subplot(426)
    pl.plot(t_timeStd, data_timeStd, color='brown')
    pl.xlabel(u"Time / h")
    pl.ylabel(u"TimeStd within 50s / V")
    pl.title(u"TimeStd(within 50s) of Diff Data of Point at" + SpacePoint)

    # 获取风舞差分信号timeRMS
    data_timeRMS = np.genfromtxt(files_timeRMS[i])
    data_timeRMS = np.array(data_timeRMS)
    data_timeRMS = np.transpose(data_timeRMS)
    data_timeRMS = data_timeRMS.reshape(72 * 24)

    t_timeRMS = np.arange(0, 24, 24.0 / (72 * 24))

    # 绘制风舞差分信号timeRMS波形
    pl.subplot(427)
    pl.plot(t_timeRMS, data_timeRMS, color='green')
    pl.xlabel(u"Time / h")
    pl.ylabel(u"TimeRMS within 50s / V")
    pl.title(u"TimeRMS(within 50s) of Diff Data of Point at" + SpacePoint)

    # timeRMS和timeStd的差值
    pl.subplot(428)
    pl.plot(t_timeRMS, data_timeRMS-data_timeStd, color="black")
    pl.xlabel(u"Time / h")
    pl.ylabel(u"Diff / V")
    pl.title(u"Diff of TimeRMS and TimeStd (TimeRMS - TimeStd) of Point at" + SpacePoint)

    pl.subplots_adjust(hspace=0.6)
    pl.savefig(u"batchPics/timeDomain/Time-Domain Plot of Point at " + SpacePoint + u".jpg")
