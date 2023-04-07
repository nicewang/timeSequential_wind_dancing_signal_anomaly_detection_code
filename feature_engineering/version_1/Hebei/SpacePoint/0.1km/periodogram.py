from scikits.talkbox.spectral import basic
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

data_periodogram = basic.periodogram(data, fs=fs)
psd, fgrid = basic.periodogram(data, fs=fs)

data_fft_periodogram = basic.periodogram(data_fft, fs=fs)
psd_fft, fgrid_fft = basic.periodogram(data_fft, fs=fs)

print fs

pl.figure(figsize=(12,8))

pl.subplot(421)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(423)
pl.plot(data_periodogram)
pl.title(u"periodogram")

pl.subplot(425)
pl.plot(data_fft_periodogram)
pl.title(u"periodogram (fft)")

pl.subplot(422)
pl.plot(psd)
pl.title(u"psd")

pl.subplot(424)
pl.plot(psd_fft)
pl.title(u"psd (fft)")

pl.subplot(426)
pl.plot(fgrid)
pl.title(u"Frequency Grid")

pl.subplot(428)
pl.plot(fgrid_fft)
pl.title(u"Frequency Grid (fft)")

pl.subplots_adjust(hspace=0.6)
pl.show()
