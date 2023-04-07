# -*- coding: utf-8 -*-
from travelFolder import *
import numpy as np
import pylab as pl
from scikits.talkbox import features
import sys

path = ''
files = travel_txt(path)
list_files(files)

pl.figure(figsize=(24,36))

title = np.array(['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th'],
                 np.str)

for i in np.arange(files.shape[0]):

    if i < 2:
        i_ = i
    elif i < 12:
        i_ = i - 2 + 10
    elif i == 12:
        i_ = 2
    elif i < 17:
        i_ = i - 13 + 20
    else:
        i_ = i - 17 + 3

    data = np.genfromtxt(files[i])
    data = np.array(data)
    data = np.diff(data)

    fs = data.shape[0]
    fs = fs / 3600.0

    # 计算梅尔倒谱系数
    ceps, mspec, spec = features.mfcc(data)
    ceps = ceps[:, int(sys.argv[1])]

    pl.subplot(8,3,i_+1)
    pl.plot(ceps, color='blue')
    pl.title(title[int(sys.argv[1])]+u" MFCC Coefficient of Diff Data within "+str(i_)+u"-"+str(i_+1)+" (Point at 24.1km)")

pl.subplots_adjust(hspace=0.6)
pl.savefig(title[int(sys.argv[1])]+u" MFCC Coefficient of Diff Data of Point at 24.1km.jpg")
