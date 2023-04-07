# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from scipy import fftpack

t = np.arange(0, 0.3, 1/20000.0)
x = np.sin(2*np.pi*1000*t) * (np.sin(2*np.pi*10*t) + np.sin(2*np.pi*7*t) + 3.0)
hx = fftpack.hilbert(x)

t1 = np.linspace(0, 8*np.pi, 1024, endpoint=False)
x1 = np.sin(t1)
y = fftpack.hilbert(x1)

sampling_rate = 8000
fft_size = 512

xs = x1[:fft_size]
xf = np.fft.rfft(xs)/fft_size
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1)
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

xs1 = y[:fft_size]
xf1 = np.fft.rfft(xs1)/fft_size
freqs1 = np.linspace(0, sampling_rate/2, fft_size/2+1)
xfp1 = 20*np.log10(np.clip(np.abs(xf1), 1e-20, 1e100))

pl.figure(figsize=(8,8))

pl.subplot(411)
pl.plot(x, label=u"Carrier Signal")
pl.plot(np.sqrt(x**2 + hx**2), "r", linewidth=2, label=u"Envelope Signal")
pl.title(u"Hilbert Transform")
pl.legend()

pl.subplot(412)
pl.plot(x1, label=u"Original Wave")
pl.plot(y, label=u"Wave after Hilbert Transforming")
pl.legend()

pl.subplot(413)
pl.plot(freqs, xfp, label=u"FFT of Origianl Signal")
pl.legend()

pl.subplot(414)
pl.plot(freqs1, xfp1, label=u"FFT of Signal after Hilbert Transforming")
pl.legend()

pl.subplots_adjust(hspace=0.4)
pl.show()
