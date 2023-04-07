# -*- coding: utf-8 -*-
# 包裹时特征选择
from sklearn.feature_selection import RFE
from sklearn.svm import LinearSVC # 选择svm作为评定算法
from sklearn.datasets import load_iris # 加载数据集
import pylab as pl

iris = load_iris()
x = iris.data
y = iris.target
estimator = LinearSVC()
selector = RFE(estimator=estimator,n_features_to_select=2)  # 选择2个特征
selector.fit(x,y)
n_features_ = selector.n_features_ # 给出被选出的特征的数量
print n_features_.shape
print n_features_
support_ = selector.support_ # 给出了被选择特征的mask
print support_.shape
print support_
ranking_ = selector.ranking_ # 特征排名，被选出特征的排名为1
print ranking_.shape
print ranking_
featureSelections = selector.transform(x)
print featureSelections.shape
print featureSelections
x_s = selector.inverse_transform(featureSelections)
print x_s.shape
print x_s

pl.figure(figsize=(8,6))

pl.subplot(321)
pl.plot(x)
pl.title(u"Iris Data")

pl.subplot(322)
pl.plot(y)
pl.title(u"Iris Target")

pl.subplot(323)
pl.plot(support_)
pl.title(u"support_")

pl.subplot(324)
pl.plot(ranking_)
pl.title(u"ranking_")

pl.subplot(325)
pl.plot(featureSelections)
pl.title(u"featureSelections")

pl.subplot(326)
pl.plot(x_s)
pl.title(u"Iris Data Back!")

pl.subplots_adjust(hspace=0.4)
pl.show()
