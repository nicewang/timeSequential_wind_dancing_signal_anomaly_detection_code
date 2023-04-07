import numpy as np
import pylab as pl
from sklearn.preprocessing import FunctionTransformer

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)
data = data.reshape(data.shape[0],1)

fft_size = data.shape[0]
t = np.arange(0, 24.0, 24.0/fft_size)

transformer = FunctionTransformer(np.log1p)
featureSelection = transformer.transform(data)

transformer0 = FunctionTransformer(np.log2)
featureSelection0 = transformer0.transform(data)

transformer1 = FunctionTransformer(np.log10)
featureSelection1 = transformer1.transform(data)

pl.figure(figsize=(8,8))

pl.subplot(411)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(412)
pl.plot(t, featureSelection)
pl.title(u"featureSelection of log1p Transformer")

pl.subplot(413)
pl.plot(t, featureSelection0)
pl.title(u"featureSelection of log2 Transformer")

pl.subplot(414)
pl.plot(t, featureSelection1)
pl.title(u"featureSelection of log10 Transformer")

pl.subplots_adjust(hspace=0.4)
pl.show()
