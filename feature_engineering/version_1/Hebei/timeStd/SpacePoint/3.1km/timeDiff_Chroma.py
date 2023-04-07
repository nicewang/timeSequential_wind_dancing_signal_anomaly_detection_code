# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from librosa.feature import spectral
from librosa.display import *

pl.figure(figsize=(8, 8))

# 获取原始风舞信号和风舞差分信号
data = np.genfromtxt("timeStd_of_Point_at_3.1km.txt")
data = np.array(data)
data = np.transpose(data)
data = data.reshape(72 * 24)
# data = np.array(data)
# data_o = data
# data = np.diff(data)
# data = data[0:7200]

t = np.arange(0, 24.0, 24.0 / data.shape[0])

fs = data.shape[0]
fs = fs / (24 * 3600.0)

chroma_gram = spectral.chroma_stft(y=data, sr=fs, n_fft=18, hop_length=18)

pl.subplot(212)
specshow(chroma_gram, y_axis='chroma', x_axis='time', hop_length=1536)
pl.xlabel(u"Time / h")
#pl.colorbar()
pl.title('Chroma Gram of Diff Data of Point at 3.1km')
pl.tight_layout()

pl.subplot(211)
pl.plot(t, data, color="blue")
# pl.plot(data, color="blue")
pl.xlim(0, 24.0)
# pl.xlim(0, data.shape[0])
pl.xlabel(u"Time / h")
pl.ylabel(u"Amplitude / V")
pl.title(u"Diff Data of Wind Wave of Point at 3.1km")

pl.subplots_adjust(hspace=0.2)
pl.show()
