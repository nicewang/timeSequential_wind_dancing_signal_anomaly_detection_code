from sklearn import preprocessing
import numpy as np
import pylab as pl

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)
data = data.reshape(data.shape[0],1)

data_scaled = preprocessing.scale(data)

fft_size = data.shape[0]
t = np.arange(0, 24.0, 24.0/fft_size)

scaler = preprocessing.StandardScaler().fit(data)
featureSelection = scaler.transform(data)

min_max_scaler = preprocessing.MinMaxScaler()
featureSelection_minmax = min_max_scaler.fit_transform(data)

max_abs_scaler = preprocessing.MaxAbsScaler()
featureSelection_maxabs = max_abs_scaler.fit_transform(data)

pl.figure(figsize=(12,8))

pl.subplot(431)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(432)
pl.plot(t, data_scaled)
pl.title(u"Scaled Diff Data")

pl.subplot(433)
pl.plot(t, featureSelection)
pl.title(u"featureSelection of StandardScaler")

pl.subplot(434)
pl.plot(t, featureSelection_minmax)
pl.title(u"featureSelection of MinMaxScaler")

pl.subplot(435)
pl.plot(t, featureSelection_maxabs)
pl.title(u"featureSelection of MaxAbsScaler")

pl.subplots_adjust(hspace=0.4)
pl.show()
