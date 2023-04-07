import numpy as np
# import pylab as pl

path = 'timeStd_of_Point_at_3.1km.txt'
data = np.genfromtxt(path)
data = np.transpose(data)
data = data.reshape(72*24,)

up = np.percentile(data,75)
down = np.percentile(data,25)

IQR = up - down

labels = np.zeros(data.shape[0])

for i in range(data.shape[0]):
    if data[i] > up + IQR*1.5:
        labels[i] = 1
    else:
        labels[i] = 0

np.savetxt('labels/mild_outliers/labels of point at 3.1km.txt',labels)

# pl.xlim(0, data.shape[0])
# for i in range(72*24):
#     if labels[i] == 2:
#         pl.bar(i,data[i],1,color='red')
#     else:
#         pl.bar(i,data[i],1,color='blue')
#
# pl.show()