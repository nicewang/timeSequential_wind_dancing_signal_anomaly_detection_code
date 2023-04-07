# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from travel_txt_demo import travel_txt, list_files
from scikits.talkbox.linpred import py_lpc

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

    data = np.genfromtxt(files_original[i])
    data = np.array(data)
    data_o = data
    data = np.diff(data)

    data_new = []
    for i in np.arange(0, 172792, 2400):
        if i < 170400:
            data_tmp = data[i:i + 2400]
        else:
            data_tmp = data[i:]
        data1 = py_lpc.lpc_ref(data_tmp, 10)
        data1 = data1[1:]
        data1 = data1.mean(0)
        if data_new == []:
            data_new = data1
        else:
            data_new = np.row_stack((data_new, data1))

    t = np.arange(0, 24.0, 24.0 / data_new.shape[0])

    pl.subplot(5,2,count)
    pl.plot(t, data_new, color='black')
    pl.xlabel(u"Time / h")
    pl.ylabel(u"10-LPC Average")
    pl.title(u"10-LPC Coefficients Average within 1200s of Diff Data of Point at" + SpacePoint)

pl.subplots_adjust(hspace=0.6)
pl.savefig(u"batchPics/timeDomain/LPC/10-LPC Coefficients Average within 1200s Plot.jpg")
