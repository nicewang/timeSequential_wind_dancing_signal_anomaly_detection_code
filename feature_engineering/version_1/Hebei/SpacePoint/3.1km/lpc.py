from scikits.talkbox.linpred import common,levinson_lpc,py_lpc
import numpy as np
import pylab as pl

path = "Data_of_Point_at_3.1km.txt"
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

a, e, k = levinson_lpc.lpc(data, 100)

a_fft, e_fft, k_fft = levinson_lpc.lpc(data_fft, 100)

pl.figure(figsize=(8,8))

pl.subplot(511)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(512)
pl.plot(a)
pl.title(u"100 Order LPC Inversion Solution")

pl.subplot(513)
pl.plot(k)
pl.title(u"100 Order LPC Reflection Coefficients")

pl.subplot(514)
pl.plot(a_fft)
pl.title(u"100 Order LPC Inversion Solution (fft)")

pl.subplot(515)
pl.plot(k_fft)
pl.title(u"100 Order LPC Reflection Coefficients (fft)")

pl.subplots_adjust(hspace=0.6)
pl.show()
