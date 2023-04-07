from scikits.talkbox.tools import correlations
import numpy as np
import pylab as pl

path = "Data_of_Point_at_0.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)

fs = data.shape[0]
fs = fs / (24*3600.0)

sampling_rate = fs
fft_size = data.shape[0]

t = np.arange(0, 24.0, 24.0/fft_size)
xs = data

xf = np.fft.rfft(xs)
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1)
data_fft = np.clip(np.abs(xf), 1e-20, 1e100)
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
xfp1 = 20*np.log10(np.clip(np.abs(xf/fft_size), 1e-20, 1e100))

data_autocorrelation = correlations.acorr(data)
data_fft_autocorrelation = correlations.acorr(data_fft)

data_nextpow2 = correlations.nextpow2(abs(data))
data_fft_nextpow2 = correlations.nextpow2(abs(data_fft))

pl.figure(figsize=(8,8))

pl.subplot(511)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(512)
pl.plot(data_autocorrelation)
pl.title(u"Data AutoCorrelation")

pl.subplot(513)
pl.plot(data_fft_autocorrelation)
pl.title(u"Data AutoCorrelation (fft)")

pl.subplot(514)
pl.plot(data_nextpow2)
pl.title(u"Data NextPow2")

pl.subplot(515)
pl.plot(data_fft_nextpow2)
pl.title(u"Data NextPow2 (fft)")

pl.subplots_adjust(hspace=0.5)
pl.show()
