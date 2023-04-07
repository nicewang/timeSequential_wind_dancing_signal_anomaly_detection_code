# -*- coding: utf-8 -*-
from librosa.feature import spectral
from librosa.display import *
import numpy as np
import pylab as pl

data = np.genfromtxt('freqCorr/freq corr of point at 3.6km.txt')

pl.subplot(311)
pl.xlim(0, data.shape[0])
x = 0.64*np.ones(data.shape[0])
pl.plot(data)
pl.plot(x, color='red')
pl.ylabel(u'Corr')
pl.title(u'CorrGram and ChromaGram of Point at 3.6km')
pl.annotate(r'$Corr=0.64$', xy=(200, 0.64), xycoords='data', xytext=(0, +13),
             textcoords='offset points', fontsize=10,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

pl.subplot(312)
pl.xlim(0, data.shape[0])
pl.ylim(0.64)
pl.plot(data)
pl.ylabel(u'Corr')

path = "original_onePointData/Data_of_Point_at_3.6km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data = np.diff(data)

t = np.arange(0, 24.0, 24.0 / data.shape[0])

fs = data.shape[0]
fs = fs / (24 * 3600.0)

chroma_gram = spectral.chroma_stft(y=data, sr=fs, n_fft=1600, hop_length=100)
print(chroma_gram.shape)

pl.subplot(313)
specshow(chroma_gram, y_axis='chroma', x_axis='time', hop_length=1536*12)
pl.xlabel(u"Time / h")
#pl.colorbar()
# pl.tight_layout()

pl.subplots_adjust(hspace=0.4)
pl.savefig(u'pic/CorrGram and ChromaGram of Point at 3.6km.png')