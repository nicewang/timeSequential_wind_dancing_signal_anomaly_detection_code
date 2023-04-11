import pylab as pl
import numpy as np

data = np.genfromtxt('freq corr of point at 3.6km.txt')

# x = np.linspace(0,1728,1728)
pl.xlim(0, data.shape[0])
# pl.ylim(0.6)
pl.plot(data)

# x = 0.65*np.ones(data.shape[0])
# pl.plot(x, color='red')

pl.show()