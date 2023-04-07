# -*- coding: utf-8 -*-
from sklearn.feature_selection import VarianceThreshold
import numpy as np
import pylab as pl

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)
data = data.reshape(data.shape[0],1)

selector = VarianceThreshold(1) # 方差阈值
selector.fit(data)
featureVar = selector.variances_ # 展现属性的方差
featureSelections = selector.transform(data) # 进行特征选择
featureIndex = selector.get_support(True) # 选择结果后，特征之前的索引
data_s = selector.inverse_transform(featureSelections)  # 将特征选择后的结果还原成原始数据
                                                        # 被剔除掉的数据，显示为0

fft_size = data.shape[0]
t = np.arange(0, 24.0, 24.0/fft_size)

pl.figure(figsize=(8,6))

pl.subplot(311)
pl.plot(t, data)
pl.title(u"Wind Waving Diff Signal")

pl.subplot(312)
pl.plot(t, featureSelections)
pl.title(u"Wind Waving Diff Signal after Features Selection")

pl.subplot(313)
pl.plot(t, data_s)
pl.title(u"Wind Waving Diff Signal Back")

pl.subplots_adjust(hspace=0.4)
pl.show()
