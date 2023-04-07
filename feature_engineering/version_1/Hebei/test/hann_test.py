import pylab as pl
import scipy.signal as signal
import numpy as np

t = np.arange(0, 1.0, 1.0/8000)
x = np.sin(2*np.pi*50*t)[:512] * signal.hann(512, sym=0)
pl.figure(figsize=(8,3))
pl.plot(np.hstack([x,x,x]))
pl.show()
