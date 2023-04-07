from scikits.talkbox.linpred import common
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

res = common.lpcres(data, 100)

data_e = data - res

res_fft = common.lpcres(data_fft, 100)

data_fft_e = data_fft - res_fft

pl.figure(figsize=(8,8))

pl.subplot(511)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(512)
pl.plot(t, res)
pl.title(u"100 Order LPC Residual")

pl.subplot(513)
pl.plot(freqs, res_fft)
pl.title(u"100 Order LPC Residual (fft)")

pl.subplot(514)
pl.plot(t, data_e)
pl.title(u"Data of 100 Order LP(Linear Prediction)")

pl.subplot(515)
pl.plot(freqs, data_fft_e)
pl.title(u"Data of 100 Order LP(Linear Prediction) (fft)")

pl.subplots_adjust(hspace=0.5)
pl.show()
