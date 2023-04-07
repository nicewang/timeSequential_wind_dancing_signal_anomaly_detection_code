import numpy as np
import pylab as pl

path = 'labels of point at 3.6 km.txt'
data = np.genfromtxt(path)

for i in range(data.shape[0]):
    if data[i] == 0:
        pl.bar(i,data[i],1,color='blue')
    else:
        pl.bar(i,data[i],1,color='red')

pl.show()