import pylab as pl
import numpy as np

mark = ['ob', 'or', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']

data = np.genfromtxt("2 clusters of point at 3.1km.txt")
for i in range(data.shape[0]):
    pl.plot(data[i,0],data[i,1], mark[np.int(data[i,2])])
pl.xlabel("timeStd / V")
pl.ylabel("freqCorr")
pl.show()