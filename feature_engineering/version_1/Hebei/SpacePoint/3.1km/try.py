import numpy as np
import pylab as pl
import scipy.signal as signal
from scipy import fftpack

def average_fft(x, fft_size):
    n = len(x) // fft_size * fft_size
    tmp = x[:n].reshape(-1, fft_size)
    tmp *= signal.hann(fft_size, sym=0)
    xf = np.abs(np.fft.rfft(tmp)/fft_size)
    avgf = np.average(xf, axis=0)
    #return 20*np.log10(avgf)
    return avgf

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)

fs = data.shape[0]
fs = fs / (24*3600.0)

sampling_rate = fs
fft_size = data.shape[0]

t0 = np.arange(0, 24.0, 24.0/data_o.shape[0])

t = np.arange(0, 24.0, 24.0/fft_size)
xs = data

xf = np.fft.rfft(xs)/fft_size
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1)
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

xf_avg = average_fft(xs, fft_size)

hx = fftpack.hilbert(xs)

xf1 = np.fft.rfft(hx)/fft_size
freqs1 = np.linspace(0, sampling_rate/2, fft_size/2+1)
xfp1 = 20*np.log10(np.clip(np.abs(xf1), 1e-20, 1e100))
xfp2 = 20*np.log10(np.abs(xf1))

print xfp1
print xfp2

pl.figure(figsize=(8,8))

pl.subplot(411)
pl.plot(t0, data_o)
pl.title(u"Signal Analysis")
pl.xlabel(u"Time/h")

pl.subplot(412)
pl.plot(t[:fft_size], xs)
pl.xlabel(u"Time/h")

pl.subplot(413)
pl.plot(freqs, abs(xf))
pl.xlabel(u"Frequency/Hz")

"""pl.subplot(515)
pl.plot(freqs, xf_avg)
pl.xlabel(u"Frequency/Hz")"""

"""pl.subplot(414)
pl.plot(np.clip(np.abs(xf), 1e-20, 1e100), label=u"Carrier Signal")
pl.plot(hx, "g", linewidth=2, label=u"Envelope Signal")
pl.legend()"""

pl.subplot(414)
pl.plot(freqs1, np.clip(np.abs(xf1), 1e-20, 1e100))
pl.xlabel(u"Frequency/Hz")

pl.subplots_adjust(hspace=0.4)
pl.show()
