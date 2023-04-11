import pylab as pl
import numpy as np

data = np.genfromtxt("timeStd_of_Point_at_3.1km.txt")
print(data.shape)
data = np.transpose(data)
data = data.reshape(1728,)
pl.plot(data)
pl.show()
