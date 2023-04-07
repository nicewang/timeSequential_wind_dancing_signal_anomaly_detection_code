# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from scipy import fftpack

t1 = np.linspace(0, 8*np.pi, 1024, endpoint=False)
x1 = np.sin(t1)
y = fftpack.hilbert(x1)

pl.plot(x1, label=u"Original Wave")
pl.plot(y, label=u"Wave after Hilbert Transforming")

pl.legend()
pl.show()
