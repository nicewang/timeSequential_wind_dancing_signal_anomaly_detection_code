import numpy as np
import scipy.signal as signal
import pylab as pl

def average_fft(x, fft_size):
    n = len(x) // fft_size * fft_size
    tmp = x[:n].reshape(-1, fft_size)
    tmp *= signal.hann(fft_size, sym=0)
    xf = np.abs(np.fft.rfft(tmp)/fft_size)
    avgf = np.average(xf, axis=0)
    return 20*np.log10(avgf)

x = np.random.rand(100000) - 0.5
xf = average_fft(x, 512)
pl.figure(figsize=(8,4))
pl.plot(xf)
pl.ylabel(u"Amplitude / dB")
pl.xlabel(u"Frequecy / Hz")
pl.show()
