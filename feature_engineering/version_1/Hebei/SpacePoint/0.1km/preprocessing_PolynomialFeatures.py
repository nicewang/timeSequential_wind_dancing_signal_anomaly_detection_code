import numpy as np
from sklearn.preprocessing import PolynomialFeatures
import pylab as pl

path = "Data_of_Point_at_0.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)
data = data.reshape(data.shape[0],1)

fft_size = data.shape[0]
t = np.arange(0, 24.0, 24.0/fft_size)

poly2 = PolynomialFeatures(2)
featureSelection2 = poly2.fit_transform(data)

poly3 = PolynomialFeatures(3)
featureSelection3 = poly3.fit_transform(data)

poly4 = PolynomialFeatures(4)
featureSelection4 = poly4.fit_transform(data)

pl.figure(figsize=(8,8))

pl.subplot(411)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(412)
pl.plot(t, featureSelection2)
pl.title(u"featureSelection of PolynomialFeatures (Degree=2)")

pl.subplot(413)
pl.plot(t, featureSelection3)
pl.title(u"featureSelection of PolynomialFeatures (Degree=3)")

pl.subplot(414)
pl.plot(t, featureSelection4)
pl.title(u"featureSelection of PolynomialFeatures (Degree=4)")

pl.subplots_adjust(hspace=0.4)
pl.show()
