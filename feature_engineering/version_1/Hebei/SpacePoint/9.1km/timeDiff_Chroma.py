# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from librosa.feature import spectral
from sklearn.preprocessing import PolynomialFeatures
from librosa.display import *

pl.figure(figsize=(8, 8))

# 获取原始风舞信号和风舞差分信号
data = np.genfromtxt("Data_of_Point_at_9.1km.txt")
data = np.array(data)
data_o = data
data = np.diff(data)
data = data.reshape(data.shape[0], 1)
# data = data[0:7200]

poly3 = PolynomialFeatures(3)
featureSelection3 = poly3.fit_transform(data)

t = np.arange(0, 24.0, 24.0 / data.shape[0])

fs = data.shape[0]
fs = fs / (24 * 3600.0)

chroma_gram = spectral.chroma_stft(y=featureSelection3[:,1:2].reshape(172792,), sr=fs, n_fft=600, hop_length=150)

pl.subplot(212)
specshow(chroma_gram, y_axis='chroma', x_axis='time', hop_length=1536)
pl.xlabel(u"Time / h")
#pl.colorbar()
pl.title('Chroma Gram of Diff Data of Point at 3.1km')
pl.tight_layout()

pl.subplot(211)
pl.plot(t, featureSelection3[:,1:2], color="blue")
# pl.plot(data, color="blue")
pl.xlim(0, 24.0)
# pl.xlim(0, data.shape[0])
pl.xlabel(u"Time / h")
pl.ylabel(u"Amplitude / V")
pl.title(u"Diff Data of Wind Wave of Point at 3.1km")

pl.subplots_adjust(hspace=0.2)
pl.show()
