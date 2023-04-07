from scipy.fftpack import dct
import numpy as np
import pylab as pl

path = "original_onePointData/Data_of_Point_at_0.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data = np.diff(data)

data_dct = dct(data)
max0 = max(abs(data_dct))
data_dct = data_dct / max0

fs = data.shape[0] / (24.0*3600)
fft_size = data.shape[0]

f = np.linspace(0, fs/2, fft_size)

path1 = "original_onePointData/Data_of_Point_at_3.1km.txt"
data1 = np.genfromtxt(path1)
data1 = np.array(data1)
data1 = np.diff(data1)

data_dct1 = dct(data1)
max1 = max(abs(data_dct1))
data_dct1 = data_dct1 / max1

pl.subplot(212)
pl.plot(f,data_dct1,color='blue')
pl.ylabel('Amplitude / V')
pl.xlabel('Freq / Hz')
pl.title('DCT of Point at 3.1km')

pl.subplot(211)
pl.plot(f,data_dct,color='blue')
pl.ylabel('Amplitude / V')
pl.xlabel('Freq / Hz')
pl.title('DCT of Point at 0.1km')

pl.subplots_adjust(hspace=0.6)
pl.show()