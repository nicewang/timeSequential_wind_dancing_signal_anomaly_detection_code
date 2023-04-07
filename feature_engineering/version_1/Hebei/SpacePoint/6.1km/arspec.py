from scikits.talkbox.spectral import basic
import numpy as np
import pylab as pl

path = "Data_of_Point_at_6.1km.txt"
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

data_arspec = basic.arspec(data, 100, fs=fs)
psd, fgrid = basic.arspec(data, 100, fs=fs)

data_fft_arspec = basic.arspec(data_fft, 100, fs=fs)
psd_fft, fgrid_fft = basic.arspec(data_fft, 100, fs=fs)

print fs

pl.figure(figsize=(12,8))

pl.subplot(421)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(423)
pl.plot(data_arspec)
pl.title(u"AR Specgram of 100 Order LPC")

pl.subplot(425)
pl.plot(data_fft_arspec)
pl.title(u"AR Specfram of 100 Order LPC (fft)")

pl.subplot(422)
pl.plot(psd)
pl.title(u"psd of 100 Order LPC")

pl.subplot(424)
pl.plot(psd_fft)
pl.title(u"psd of 100 Order LPC (fft)")

pl.subplot(426)
pl.plot(fgrid)
pl.title(u"Frequency Grid of 100 Order LPC")

pl.subplot(428)
pl.plot(fgrid_fft)
pl.title(u"Frequency Grid of 100 Order LPC (fft)")

pl.subplots_adjust(hspace=0.6)
pl.show()
