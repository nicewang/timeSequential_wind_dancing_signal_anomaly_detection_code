import numpy as np
import pylab as pl
from scipy import fftpack

path = "Data_of_Point_at_0.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data = np.diff(data)

fs = data.shape[0]
fs = fs / (24*3600.0)

sampling_rate = fs
fft_size = data.shape[0]

t = np.arange(0, 24.0, 24.0/fft_size)
xs = data

xf = np.fft.rfft(xs)/fft_size
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1)
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

hx = fftpack.hilbert(np.clip(np.abs(xf), 1e-20, 1e100))

pl.figure(figsize=(8,6))

pl.subplot(311)
pl.plot(t[:fft_size], xs)
pl.xlabel(u"Time/s")
pl.title(u"Plot of Wave with 156.25Hz and Wave with 234.375Hz")

pl.subplot(312)
pl.plot(freqs, np.clip(np.abs(xf), 1e-20, 1e100))
pl.xlabel(u"Frequency/Hz")

pl.subplot(313)
pl.plot(np.clip(np.abs(xf), 1e-20, 1e100), label=u"Carrier Signal")
pl.plot(np.sqrt((np.clip(np.abs(xf), 1e-20, 1e100))**2 + hx**2), "g", linewidth=2, label=u"Envelope Signal")
pl.legend()

pl.subplots_adjust(hspace=0.4)
pl.show()
