from librosa.feature import spectral
import numpy as np
import pylab as pl
from librosa.display import *
import librosa as librosa

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)

fs = data.shape[0]
fs = fs / (24*3600.0)

fft_size = data.shape[0]

t = np.arange(0, 24.0, 24.0/fft_size)

#data_zcr = spectral.zero_crossing_rate(data, frame_length=2048, hop_length=50)
data_zcr = spectral.zero_crossing_rate(data)
print data_zcr.shape
data_zcr = data_zcr.reshape(data_zcr.shape[0]*data_zcr.shape[1],)

data_spectral_centroid = spectral.spectral_centroid(data, sr=fs)
print data_spectral_centroid.shape
data_spectral_centroid = data_spectral_centroid.reshape(data_spectral_centroid.shape[0]*data_spectral_centroid.shape[1],)

data_spectral_rolloff = spectral.spectral_rolloff(data, sr=fs)
print data_spectral_rolloff.shape
data_spectral_rolloff = data_spectral_rolloff.reshape(data_spectral_rolloff.shape[0]*data_spectral_rolloff.shape[1])

mfcc = spectral.mfcc(data, sr=fs, n_mfcc=16)
print mfcc.shape

pl.figure(figsize=(8,8))

pl.subplot(411)
pl.plot(t, data)
pl.title(u"Original Diff Data")
pl.xlabel(u"Time / h")
pl.ylabel(u"Amplitude / V")

pl.subplot(412)
pl.plot(data_zcr)
pl.title(u"ZCR")

pl.subplot(413)
pl.plot(data_spectral_centroid)
pl.title(u"spectral_centroid")

pl.subplot(414)
pl.plot(data_spectral_rolloff)
pl.title(u"spectral_rolloff")

pl.subplots_adjust(hspace=0.6)
pl.show() 



pl.figure(figsize=(16,8))

pl.subplot(441)
pl.plot(mfcc[0,:])

pl.subplot(442)
pl.plot(mfcc[1,:])
pl.title(u"MFCC (16 Coefficients) of ")

pl.subplot(443)
pl.plot(mfcc[2,:])
pl.title(u"Diff Data of Point at 3.1km")

pl.subplot(444)
pl.plot(mfcc[3,:])

pl.subplot(445)
pl.plot(mfcc[4,:])

pl.subplot(446)
pl.plot(mfcc[5,:])

pl.subplot(447)
pl.plot(mfcc[6,:])

pl.subplot(448)
pl.plot(mfcc[7,:])

pl.subplot(449)
pl.plot(mfcc[8,:])

pl.subplot(4,4,10)
pl.plot(mfcc[9,:])

pl.subplot(4,4,11)
pl.plot(mfcc[10,:])

pl.subplot(4,4,12)
pl.plot(mfcc[11,:])

pl.subplot(4,4,13)
pl.plot(mfcc[12,:])



pl.subplot(4,4,14)
pl.plot(mfcc[13,:])

pl.subplot(4,4,15)
pl.plot(mfcc[14,:])

pl.subplot(4,4,16)
pl.plot(mfcc[15,:])



pl.subplots_adjust(hspace=0.4)
pl.show()

chroma_cq = spectral.chroma_stft(y=data, sr=fs)

pl.figure(figsize=(10, 4))
specshow(chroma_cq, y_axis='chroma', x_axis='time')
pl.colorbar()
pl.title('Chromagram')
pl.tight_layout()
pl.show()
