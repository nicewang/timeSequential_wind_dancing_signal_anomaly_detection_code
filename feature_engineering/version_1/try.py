import numpy as np
import matplotlib.pyplot as pl
import math
import random

row = 4
col = 4

N = 500
fs = 5
n = [2 * math.pi * fs * t / N for t in range(N)]
# print n
axis_x = np.linspace(0, 3, num=N)

x = [math.sin(i) for i in n]
pl.subplot(221)
pl.plot(axis_x, x)
pl.title('Sin Signal')
pl.axis('tight')

x1 = [random.gauss(0, 0.5) for i in range(N)]
xx = []

for i in range(len(x)):
    xx.append(x[i] * 3 + x1[i])

pl.subplot(222)
pl.plot(axis_x, xx)
pl.title('Sin Signal + Noise')
pl.axis('tight')

xf = np.fft.fft(x)
xf_abs = np.fft.fftshift(abs(xf))
axis_xf = np.linspace(-N / 2, N / 2 - 1, num=N)
pl.subplot(223)
pl.title('Frequency Signal')
pl.plot(axis_xf, xf_abs)
pl.axis('tight')

xf = np.fft.fft(xx)
xf_abs = np.fft.fftshift(abs(xf))
pl.subplot(224)
pl.title('Sin Frequency Signal')
pl.plot(axis_xf, xf_abs)
pl.axis('tight')

pl.show()
