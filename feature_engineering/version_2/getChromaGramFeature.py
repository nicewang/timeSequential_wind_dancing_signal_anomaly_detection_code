# -*- coding: utf-8 -*-
from librosa.feature import spectral
from librosa.display import *
import numpy as np
import pylab as pl

path = "original_onePointData/Data_of_Point_at_3.6km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data = np.diff(data)

t = np.arange(0, 24.0, 24.0 / data.shape[0])

fs = data.shape[0]
fs = fs / (24 * 3600.0)

chroma_gram = spectral.chroma_stft(y=data, sr=fs, n_fft=100, hop_length=100)
print(chroma_gram.shape)

# pl.subplot(211)
# specshow(chroma_gram, y_axis='chroma', x_axis='time', hop_length=1536*12)
# pl.xlabel(u"Time / h")
# # pl.colorbar()
# # pl.tight_layout()
#
# pl.subplot(212)
# pl.plot(t, data, color="blue")
# pl.xlim(0, 24.0)
# pl.xlabel(u"Time / h")
# pl.ylabel(u"Amplitude / V")
#
# pl.show()

np.savetxt('chromaFeature/100len/ChromaFeature of Point at 3.6km.txt', chroma_gram)