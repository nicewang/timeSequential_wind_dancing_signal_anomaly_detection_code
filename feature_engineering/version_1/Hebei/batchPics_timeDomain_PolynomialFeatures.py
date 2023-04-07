# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from sklearn.preprocessing import PolynomialFeatures
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

    data = np.genfromtxt(files_original[i])
    data = np.array(data)
    data_o = data
    data = np.diff(data)
    data = data.reshape(data.shape[0], 1)

    fft_size = data.shape[0]
    t = np.arange(0, 24.0, 24.0 / fft_size)

    poly2 = PolynomialFeatures(2)
    featureSelection2 = poly2.fit_transform(data)

    poly3 = PolynomialFeatures(3)
    featureSelection3 = poly3.fit_transform(data)

    poly4 = PolynomialFeatures(4)
    featureSelection4 = poly4.fit_transform(data)

    pl.figure(figsize=(16, 4))

    pl.subplot(221)
    pl.plot(t, data)
    pl.xlabel(u"Time / h")
    pl.ylabel(u"Amplitude / V")
    pl.title(u"Original Diff Data of Point at" + SpacePoint)

    pl.subplot(222)
    pl.plot(t, featureSelection2)
    pl.xlabel(u"Time / h")
    pl.title(u"Polynomial Features(Degree=2) of Diff Data of Point at" + SpacePoint)

    pl.subplot(223)
    pl.plot(t, featureSelection3)
    pl.xlabel(u"Time / h")
    pl.title(u"Polynomial Features(Degree=3) of Diff Data of Point at" + SpacePoint)


    pl.subplot(224)
    pl.plot(t, featureSelection4)
    pl.xlabel(u"Time / h")
    pl.title(u"Polynomial Features(Degree=4) of Diff Data of Point at" + SpacePoint)

    pl.subplots_adjust(hspace=0.6)
    pl.savefig(u"batchPics/timeDomain/polynomialFeatures/Polynomial Features(Degree=4) of Diff Data of Point at " + SpacePoint + u".jpg")
