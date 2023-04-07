# -*- coding: utf-8 -*-
import glob
import os
import numpy as np
import pylab as pl
from travel_txt_demo import travel_txt, list_files

path_lpc = "lpc/SpacePoint/"
files_lpc = travel_txt(path_lpc)
print "遍历文件夹files_lpc得到如下文件："
list_files(files_lpc)

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

    data_lpc = np.genfromtxt(files_lpc[i])
    data_lpc = np.array(data_lpc)
    data_lpc = np.transpose(data_lpc)
    data_lpc = data_lpc.reshape(72 * 24)

    t_lpc = np.arange(0, 24, 24.0 / (72 * 24))

    pl.subplot(5,2,count)
    pl.plot(t_lpc, data_lpc, color='black')
    pl.xlabel(u"Time / h")
    pl.ylabel(u"10-LPC Average")
    pl.title(u"10-LPC Coefficients Average within 50s of Diff Data of Point at" + SpacePoint)

pl.subplots_adjust(hspace=0.6)
pl.savefig(u"batchPics/timeDomain/LPC/10-LPC Coefficients Average Plot.jpg")
