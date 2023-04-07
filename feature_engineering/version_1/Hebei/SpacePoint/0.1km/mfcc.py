# -*- coding:utf-8 -*-
from scikits.talkbox.features import mfcc
import numpy as np
import pylab as pl

path = "Data_of_Point_at_0.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)

ceps, mspec, spec = mfcc(data)
print ceps.shape

print ceps[:,0:1].reshape(1079,)

pl.figure(figsize=(16,8))

pl.subplot(441)
pl.plot(ceps[:,0:1].reshape(1079,))

pl.subplot(442)
pl.plot(ceps[:,1:2].reshape(1079,))

pl.subplot(443)
pl.plot(ceps[:,2:3].reshape(1079,))

pl.subplot(444)
pl.plot(ceps[:,3:4].reshape(1079,))

pl.subplot(445)
pl.plot(ceps[:,4:5].reshape(1079,))

pl.subplot(446)
pl.plot(ceps[:,5:6].reshape(1079,))

pl.subplot(447)
pl.plot(ceps[:,6:7].reshape(1079,))

pl.subplot(448)
pl.plot(ceps[:,7:8].reshape(1079,))

pl.subplot(449)
pl.plot(ceps[:,8:9].reshape(1079,))

pl.subplot(4,4,10)
pl.plot(ceps[:,9:10].reshape(1079,))

pl.subplot(4,4,11)
pl.plot(ceps[:,10:11].reshape(1079,))

pl.subplot(4,4,12)
pl.plot(ceps[:,11:12].reshape(1079,))

pl.subplot(4,4,13)
pl.plot(ceps[:,12:13].reshape(1079,))

pl.subplots_adjust(hspace=0.4)
pl.show()
