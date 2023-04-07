import numpy as np
import pylab as pl
import scipy.signal as signal

sampling_rate = 8000
fft_size = 512
t = np.arange(0, 1.0, 1.0/sampling_rate)
x = np.sin(2*np.pi*200*t) + 2*np.sin(2*np.pi*300*t)
xs = x[:fft_size]
xf = np.fft.rfft(xs)/fft_size
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1)
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
pl.figure(figsize=(8,3))
pl.plot(freqs, xfp)
x_hann = x[:512] * signal.hann(512, sym=0)
pl.plot(np.hstack([x_hann,x_hann,x_hann]), color="green")
pl.xlabel(u"Frequency/Hz")
pl.show()
