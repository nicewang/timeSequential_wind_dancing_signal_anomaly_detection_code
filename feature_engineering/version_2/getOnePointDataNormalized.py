import numpy as np
import pylab as pl

path = "original_onePointData/Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data = np.diff(data)

data_timeStd = []
for i in range(1728):
    data_tmp = data[100*i:100*(i+1)]
    max_tmp = max(abs(data_tmp))
    data_tmp = data_tmp / max_tmp
    data_tmp = data_tmp.std(0)
    if data_timeStd == []:
        data_timeStd = data_tmp
    else:
        data_timeStd = np.row_stack((data_timeStd, data_tmp))

for i in range(1728):
    data_tmp = data[100*i:100*(i+1)]
    max_tmp = max(abs(data_tmp))
    data_tmp = data_tmp / max_tmp
    data[100*i:100*(i+1)] = data_tmp

pl.plot(data[11100:11200])
pl.show()
