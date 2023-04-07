# -*- coding: utf-8 -*-
import glob
import os
import numpy as np
import pylab as pl
from sklearn.preprocessing import PolynomialFeatures

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

# pl.figure(figsize=(16,16))

for i in xrange(10):

    SpacePoint = ""
    i_ = 0
    if i == 0:
        SpacePoint = "0.1km"
        i_ = 1
    elif i == 1:
        SpacePoint = "12.1km"
        i_ = 5
    elif i == 2:
        SpacePoint = "15.1km"
        i_ = 6
    elif i == 3:
        SpacePoint = "18.1km"
        i_ = 7
    elif i == 4:
        SpacePoint = "21.1km"
        i_ = 8
    elif i == 5:
        SpacePoint = "24.1km"
        i_ = 9
    elif i == 6:
        SpacePoint = "27.1km"
        i_ = 10
    elif i == 7:
        SpacePoint = "3.1km"
        i_ = 2
    elif i == 8:
        SpacePoint = "6.1km"
        i_ = 3
    else:
        SpacePoint = "9.1km"
        i_ = 4

    i_0 = ((i_-1)/2)*2+i_
    i_1 = i_0 + 2

    # pl.figure(figsize=(20,24))

    # 获取原始风舞信号和风舞差分信号
    data = np.genfromtxt(files_original[i])
    data = np.array(data)
    data_o = data
    data = np.diff(data)

    # Normalization
    max = np.max(data)
    data = data / np.float64(max)

    fs = data.shape[0]
    fs = fs / (24 * 3600.0)

    sampling_rate = fs
    fft_size = data.shape[0]

    t0 = np.arange(0, 24.0, 24.0 / data_o.shape[0])

    t = np.arange(0, 24.0, 24.0 / fft_size)

    # # 绘制原始风舞信号波形和风舞差分信号波形
    # pl.subplot(421)
    # pl.plot(t0, data_o)
    # pl.title(u"Original Data of Wind Wave of Point at" + SpacePoint)
    # pl.xlabel(u"Time / h")
    # pl.ylabel(u"Amplitude / V")

    # # pl.subplot(10,2,i_0)
    # pl.subplot(641)
    # pl.plot(t, data, color="blue")
    # pl.xlim(0, 24.0)
    # pl.title(u"Diff Data of Wind Wave of Point at" + SpacePoint)
    # pl.xlabel(u"Time / h")
    # pl.ylabel(u"Amplitude / V")

    poly4 = PolynomialFeatures(4)

    # 获取风舞差分信号timeMax
    data_timeMax = np.genfromtxt(files_timeMax[i])
    data_timeMax = np.array(data_timeMax)
    data_timeMax = np.transpose(data_timeMax)
    data_timeMax = data_timeMax.reshape(72 * 24)

    # Normalization
    max_tmax = np.max(data_timeMax)
    data_timeMax = data_timeMax / np.float64(max_tmax)
    mean_max = np.mean(data_timeMax)
    data_timeMax = data_timeMax - mean_max
    data_timeMax = np.abs(data_timeMax)

    data_timeMax = data_timeMax.reshape(72*24,1)
    f_timeMax = poly4.fit_transform(data_timeMax)

    f1_timeMax = f_timeMax[:,1:2]
    f1_timeMax = f1_timeMax.reshape(72*24,)
    f2_timeMax = f_timeMax[:,2:3]
    f2_timeMax = f2_timeMax.reshape(72*24,)
    f3_timeMax = f_timeMax[:,3:4]
    f3_timeMax = f3_timeMax.reshape(72*24,)
    f4_timeMax = f_timeMax[:,4:5]
    f4_timeMax = f4_timeMax.reshape(72*24,)

    t_timeMax = np.arange(0, 24, 24.0 / (72 * 24))

    # # 绘制风舞差分信号timeMax波形
    # pl.subplot(645)
    # pl.plot(t_timeMax, f1_timeMax, color='orange')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.ylabel(u"TimeMax within 50s / V")
    # pl.title(u"TimeMax(within 50s) of Diff Data of Point at" + SpacePoint)
    #
    # pl.subplot(646)
    # pl.plot(t_timeMax, f2_timeMax, color='orange')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"2nd PolynomialFeatures of TimeMax")
    #
    # pl.subplot(647)
    # pl.plot(t_timeMax, f3_timeMax, color='orange')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"3rd PolynomialFeatures of TimeMax")
    #
    # pl.subplot(648)
    # pl.plot(t_timeMax, f4_timeMax, color='orange')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"4th PolynomialFeatures of TimeMax")

    # 获取风舞差分信号timeMaxMin
    data_timeMaxMin = np.genfromtxt(files_timeMaxMin[i])
    data_timeMaxMin = np.array(data_timeMaxMin)
    data_timeMaxMin = np.transpose(data_timeMaxMin)
    data_timeMaxMin = data_timeMaxMin.reshape(72 * 24)

    # Normalization
    max_tmaxmin = np.max(data_timeMaxMin)
    data_timeMaxMin = data_timeMaxMin / np.float64(max_tmaxmin)
    mean_maxmin = np.mean(data_timeMaxMin)
    data_timeMaxMin = data_timeMaxMin - mean_maxmin
    data_timeMaxMin = np.abs(data_timeMaxMin)

    data_timeMaxMin = data_timeMaxMin.reshape(72*24,1)
    f_timeMaxMin = poly4.fit_transform(data_timeMaxMin)

    f1_timeMaxMin = f_timeMaxMin[:, 1:2]
    f1_timeMaxMin = f1_timeMaxMin.reshape(72 * 24, )
    f2_timeMaxMin = f_timeMaxMin[:, 2:3]
    f2_timeMaxMin = f2_timeMaxMin.reshape(72 * 24, )
    f3_timeMaxMin = f_timeMaxMin[:, 3:4]
    f3_timeMaxMin = f3_timeMaxMin.reshape(72 * 24, )
    f4_timeMaxMin = f_timeMaxMin[:, 4:5]
    f4_timeMaxMin = f4_timeMaxMin.reshape(72 * 24, )

    t_timeMaxMin = np.arange(0, 24, 24.0 / (72 * 24))

    # # 绘制风舞差分信号timeMaxMin波形
    # pl.subplot(649)
    # pl.plot(t_timeMaxMin, f1_timeMaxMin, color='red')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.ylabel(u"TimeMaxMin within 50s / V")
    # pl.title(u"TimeMaxMin(within 50s) of Diff Data of Point at" + SpacePoint)
    #
    # pl.subplot(6,4,10)
    # pl.plot(t_timeMaxMin, f2_timeMaxMin, color='red')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"2nd PolynomialFeatures of TimeMaxMin")
    #
    # pl.subplot(6, 4, 11)
    # pl.plot(t_timeMaxMin, f3_timeMaxMin, color='red')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"3rd PolynomialFeatures of TimeMaxMin")
    #
    # pl.subplot(6, 4, 12)
    # pl.plot(t_timeMaxMin, f4_timeMaxMin, color='red')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"4th PolynomialFeatures of TimeMaxMin")

    # 获取风舞差分信号timeMean
    data_timeMean = np.genfromtxt(files_timeMean[i])
    data_timeMean = np.array(data_timeMean)
    data_timeMean = np.transpose(data_timeMean)
    data_timeMean = data_timeMean.reshape(72 * 24)

    # Normalization
    max_tmean = np.max(data_timeMean)
    data_timeMean = data_timeMean / np.float64(max_tmean)
    mean_mean = np.mean(data_timeMean)
    data_timeMean = data_timeMean - mean_mean
    data_timeMean = np.abs(data_timeMean)

    data_timeMean = data_timeMean.reshape(72*24,1)
    f_timeMean = poly4.fit_transform(data_timeMean)

    f1_timeMean = f_timeMean[:, 1:2]
    f1_timeMean = f1_timeMean.reshape(72 * 24, )
    f2_timeMean = f_timeMean[:, 2:3]
    f2_timeMean = f2_timeMean.reshape(72 * 24, )
    f3_timeMean = f_timeMean[:, 3:4]
    f3_timeMean = f3_timeMean.reshape(72 * 24, )
    f4_timeMean = f_timeMean[:, 4:5]
    f4_timeMean = f4_timeMean.reshape(72 * 24, )

    t_timeMean = np.arange(0, 24, 24.0 / (72 * 24))

    # # 绘制风舞差分信号timeMean波形
    # pl.subplot(6,4,13)
    # pl.plot(t_timeMean, f1_timeMean, color='purple')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.ylabel(u"TimeMean within 50s / V")
    # pl.title(u"TimeMean(within 50s) of Diff Data of Point at" + SpacePoint)
    #
    # pl.subplot(6, 4, 14)
    # pl.plot(t_timeMean, f2_timeMean, color='purple')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"2nd PolynomialFeatures of TimeMean")
    #
    # pl.subplot(6, 4, 15)
    # pl.plot(t_timeMean, f3_timeMean, color='purple')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"3rd PolynomialFeatures of TimeMean")
    #
    # pl.subplot(6, 4, 16)
    # pl.plot(t_timeMean, f4_timeMean, color='purple')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"4th PolynomialFeatures of TimeMean")

    # 获取风舞差分信号timeStd
    data_timeStd = np.genfromtxt(files_timeStd[i])
    data_timeStd = np.array(data_timeStd)
    data_timeStd = np.transpose(data_timeStd)
    data_timeStd = data_timeStd.reshape(72 * 24)

    # Normalization
    max_tstd = np.max(data_timeStd)
    data_timeStd = data_timeStd / np.float64(max_tstd)
    mean_std = np.mean(data_timeStd)
    data_timeStd = data_timeStd - mean_std
    data_timeStd = np.abs(data_timeStd)

    data_timeStd = data_timeStd.reshape(72*24,1)
    f_timeStd = poly4.fit_transform(data_timeStd)

    f1_timeStd = f_timeStd[:, 1:2]
    f1_timeStd = f1_timeStd.reshape(72 * 24, )
    f2_timeStd = f_timeStd[:, 2:3]
    f2_timeStd = f2_timeStd.reshape(72 * 24, )
    f3_timeStd = f_timeStd[:, 3:4]
    f3_timeStd = f3_timeStd.reshape(72 * 24, )
    f4_timeStd = f_timeStd[:, 4:5]
    f4_timeStd = f4_timeStd.reshape(72 * 24, )

    t_timeStd = np.arange(0, 24, 24.0 / (72 * 24))

    # # 绘制风舞差分信号timeStd波形
    # pl.subplot(6,4,17)
    # pl.plot(t_timeStd, f1_timeStd, color='brown')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.ylabel(u"TimeStd within 50s / V")
    # pl.title(u"TimeStd(within 50s) of Diff Data of Point at" + SpacePoint)
    #
    # pl.subplot(6, 4, 18)
    # pl.plot(t_timeStd, f2_timeStd, color='brown')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"2nd PolynomialFeatures of TimeStd")
    #
    # pl.subplot(6, 4, 19)
    # pl.plot(t_timeStd, f3_timeStd, color='brown')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"3rd PolynomialFeatures of TimeStd")
    #
    # pl.subplot(6, 4, 20)
    # pl.plot(t_timeStd, f4_timeStd, color='brown')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"4th PolynomialFeatures of TimeStd")

    # 获取风舞差分信号timeRMS
    data_timeRMS = np.genfromtxt(files_timeRMS[i])
    data_timeRMS = np.array(data_timeRMS)
    data_timeRMS = np.transpose(data_timeRMS)
    data_timeRMS = data_timeRMS.reshape(72 * 24)

    # Normalization
    max_trms = np.max(data_timeRMS)
    data_timeRMS = data_timeRMS / np.float64(max_trms)
    mean_rms = np.mean(data_timeRMS)
    data_timeRMS = data_timeRMS - mean_rms
    data_timeRMS = np.abs(data_timeRMS)

    data_timeRMS = data_timeRMS.reshape(72*24,1)
    f_timeRMS = poly4.fit_transform(data_timeRMS)

    f1_timeRMS = f_timeRMS[:, 1:2]
    f1_timeRMS = f1_timeRMS.reshape(72 * 24, )
    f2_timeRMS = f_timeRMS[:, 2:3]
    f2_timeRMS = f2_timeRMS.reshape(72 * 24, )
    f3_timeRMS = f_timeRMS[:, 3:4]
    f3_timeRMS = f3_timeRMS.reshape(72 * 24, )
    f4_timeRMS = f_timeRMS[:, 4:5]
    f4_timeRMS = f4_timeRMS.reshape(72 * 24, )

    t_timeRMS = np.arange(0, 24, 24.0 / (72 * 24))

    # # 绘制风舞差分信号timeRMS波形
    # pl.subplot(6,4,21)
    # pl.plot(t_timeRMS, f1_timeRMS, color='green')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.ylabel(u"TimeRMS within 50s / V")
    # pl.title(u"TimeRMS(within 50s) of Diff Data of Point at" + SpacePoint)
    #
    # pl.subplot(6, 4, 22)
    # pl.plot(t_timeRMS, f2_timeRMS, color='green')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"2nd PolynomialFeatures of TimeRMS")
    #
    # pl.subplot(6, 4, 23)
    # pl.plot(t_timeRMS, f3_timeRMS, color='green')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"3rd PolynomialFeatures of TimeRMS")
    #
    # pl.subplot(6, 4, 24)
    # pl.plot(t_timeRMS, f4_timeRMS, color='green')
    # pl.xlim(0, 24.0)
    # pl.xlabel(u"Time / h")
    # pl.title(u"4th PolynomialFeatures of TimeRMS")

    data_new = f1_timeMax
    data_new = np.row_stack((data_new, f2_timeMax))
    data_new = np.row_stack((data_new, f3_timeMax))
    data_new = np.row_stack((data_new, f4_timeMax))
    data_new = np.row_stack((data_new, f1_timeMaxMin))
    data_new = np.row_stack((data_new, f2_timeMaxMin))
    data_new = np.row_stack((data_new, f3_timeMaxMin))
    data_new = np.row_stack((data_new, f4_timeMaxMin))
    data_new = np.row_stack((data_new, f1_timeMean))
    data_new = np.row_stack((data_new, f2_timeMean))
    data_new = np.row_stack((data_new, f3_timeMean))
    data_new = np.row_stack((data_new, f4_timeMean))
    data_new = np.row_stack((data_new, f1_timeStd))
    data_new = np.row_stack((data_new, f2_timeStd))
    data_new = np.row_stack((data_new, f3_timeStd))
    data_new = np.row_stack((data_new, f4_timeStd))
    data_new = np.row_stack((data_new, f1_timeRMS))
    data_new = np.row_stack((data_new, f2_timeRMS))
    data_new = np.row_stack((data_new, f3_timeRMS))
    data_new = np.row_stack((data_new, f4_timeRMS))
    data_new = data_new*255.0

    # data_tmp = data_new
    # for i in xrange(10):
    #     data_new = np.row_stack((data_new, data_tmp))

    t_new = np.arange(0, 24.0, 24.0/ (72*24))

    np.savetxt(u"features/compound/timeDomain/Compound-Features of Point at" + SpacePoint + u".txt", data_new)

    # pl.subplot(211)
    # pl.imshow(data_new[:,12:18], cmap='gray')
    # pl.title(u"Compound-Features at 00:10 to 00:15 of Point at" + SpacePoint)
    #
    # pl.subplot(212)
    # pl.imshow(data_new[:,192:198], cmap='gray')
    # pl.title(u"Compound-Features at 15:10 to 15:15 of Point at" + SpacePoint)

    # pl.subplots_adjust(hspace=0.6)
    # pl.savefig("tmp/" + SpacePoint + ".jpg")

    # pl.subplot(10,2,i_1)
    # pl.imshow(data_new, cmap='gray')
    # pl.show()

    # pl.subplots_adjust(hspace=0.4)
    # pl.savefig("tmp/" + SpacePoint + ".jpg")

# pl.subplots_adjust(hspace=0.4)
# pl.savefig("tmp/tmp.jpg")
