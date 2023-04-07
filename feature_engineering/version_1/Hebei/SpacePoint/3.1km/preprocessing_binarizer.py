from sklearn import preprocessing
import numpy as np
import pylab as pl

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)
data = data.reshape(data.shape[0],1)

fft_size = data.shape[0]
t = np.arange(0, 24.0, 24.0/fft_size)

binarizer = preprocessing.Binarizer().fit(data)
featureSelection = binarizer.transform(data)

binarizer1 = preprocessing.Binarizer(threshold=1.1)
featureSelection1 = binarizer1.transform(data)

pl.figure(figsize=(12,8))

pl.subplot(431)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(432)
pl.plot(t, featureSelection)
pl.title(u"featureSelection of Binarizer")

pl.subplot(433)
pl.plot(t, featureSelection1)
pl.title(u"featureSelection of Binarizer with Threshold 1.1")

pl.subplots_adjust(hspace=0.4)
pl.show()
