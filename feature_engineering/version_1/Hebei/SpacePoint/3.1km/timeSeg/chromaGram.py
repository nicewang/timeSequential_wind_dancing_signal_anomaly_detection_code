# -*- coding: utf-8 -*-
from travelFolder import *
from librosa.feature import spectral
from librosa.display import *
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
    fs = fs / (24 * 3600.0)

    chroma_gram = spectral.chroma_stft(y=data, sr=fs, n_fft=200, hop_length=50)

    t_chromagram = np.arange(i_, i_ + 1, 1.0 / chroma_gram.shape[1])

    # 绘制频谱中心图
    pl.subplot(12, 2, i_ + 1)
    specshow(chroma_gram, y_axis='chroma', x_axis='time')
    if i_ == 14 or i_ == 16:
        pl.title(u"Spectral Centroid Plot within " + str(i_) + u"-" + str(i_ + 1) + " (Point at 3.1km)", color='red')
    elif i_ == 15:
        pl.title(u"Spectral Centroid Plot within " + str(i_) + u"-" + str(i_ + 1) + " (Point at 3.1km)", color='orange')
    else:
        pl.title(u"Spectral Centroid Plot within " + str(i_) + u"-" + str(i_ + 1) + " (Point at 3.1km)", color='blue')
        #pl.semilogy(t_scentroid, data_spectral_centroid, color='blue', label='frame_len=100s,hop_len=25s')
    pl.xlabel(u"Time / h")
    pl.colorbar()
    pl.tight_layout()

pl.subplots_adjust(hspace=0.6)
pl.savefig(u"Spectral Centroid Plot of Point at 3.1km.jpg")
