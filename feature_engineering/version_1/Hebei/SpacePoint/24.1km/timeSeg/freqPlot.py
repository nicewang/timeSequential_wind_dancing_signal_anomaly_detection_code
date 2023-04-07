# -*- coding: utf-8 -*-
from travelFolder import *
import numpy as np
import pylab as pl

path = ''
files = travel_txt(path)
list_files(files)

pl.figure(figsize=(24,36))

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

    sampling_rate = fs
    fft_size = data.shape[0]

    xs = data
    # 进行快速傅立叶变换
    xf = np.fft.rfft(xs)

    freqs = np.linspace(0, sampling_rate / 2, fft_size / 2 + 1)

    pl.subplot(8,3,i_+1)
    pl.plot(freqs, np.abs(xf), color='blue')
    pl.xlabel(u"Frequency / Hz")
    pl.ylabel(u"Amplitude / V")
    pl.title(u"Freq Plot within "+str(i_)+u"-"+str(i_+1)+" (Point at 24.1km)")

pl.subplots_adjust(hspace=0.6)
pl.savefig(u"Freq Plot of Point at 24.1km.jpg")
