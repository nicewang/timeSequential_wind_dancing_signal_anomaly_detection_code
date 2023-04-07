import numpy as np
import pylab as pl

path = 'timeStd/timeStd_of_Point_at_9.1km.txt'
data = np.genfromtxt(path)
data = np.transpose(data)
data = data.reshape(72*24,)

labels = np.genfromtxt('timeStd/labels/extreme_outliers/labels of point at 9.1km.txt')

count = 0
pl.xlim(0, data.shape[0])
for i in range(72*24):
    if labels[i] == 1:
        pl.bar(i,data[i],1,color='red')
        count = count + 1
    else:
        pl.bar(i,data[i],1,color='blue')

print(count)
pl.show()