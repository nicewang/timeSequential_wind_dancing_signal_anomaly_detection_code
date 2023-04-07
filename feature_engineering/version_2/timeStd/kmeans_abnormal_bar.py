import numpy as np
import cv2
import pylab as pl

path = 'timeStd_of_Point_at_12.1km.txt'
data = np.genfromtxt(path)
data = np.transpose(data)
data = data.reshape(72*24,1)
data = np.float32(data)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
flags = cv2.KMEANS_RANDOM_CENTERS

compactness,labels,centers = cv2.kmeans(data,2,None,criteria,10,flags)

# print(labels.shape)
# print(labels)

# labels = np.genfromtxt('labels/fr_kmeans_and_chroma/labels of point at 3.6 km.txt')

labels = np.ones(labels.shape) - labels
labels = np.int8(labels)

# print(labels.shape)
# print(labels)

pl.subplot(211)
pl.xlim(0,data.shape[0])
pl.plot(data)

pl.subplot(212)
pl.xlim(0,data.shape[0])
for i in range(72*24):
    if labels[i] == 1:
        # pl.scatter(i,data[i],color='blue',alpha=0.1)
        pl.bar(i,data[i],1,color='red')
    else:
        # pl.scatter(i,data[i],color='red',alpha=0.1)
        pl.bar(i,data[i],1,color='blue')

pl.show()

# print(labels[1531])
np.savetxt('labels/labels of point at 12.1km.txt',labels)
# np.savetxt('labels/tmp.txt',labels)