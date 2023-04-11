import pylab as pl
import numpy as np

mark = ['og', 'ob', 'or', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']

data = np.genfromtxt("3 clusters of point at 3.6km.txt")
for i in range(data.shape[0]):
    pl.plot(data[i,0],data[i,1], mark[np.int(data[i,2])])
pl.xlabel("timeStd / V")
pl.ylabel("freqCorr")
pl.show()