# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from sklearn.preprocessing import PolynomialFeatures
import cv2

a = np.array([[1.2, 2.3], [3.4, 4.5]])
a_max = np.max(a)
print a_max

# 获取原始风舞信号和风舞差分信号
data_0 = np.genfromtxt("Data_of_Point_at_3.1km.txt")
data_0 = np.array(data_0)
data_0 = np.diff(data_0)
# data_0 = np.abs(data_0)
# max = np.max(data_0)
# print max
# data_0 = data_0 / max
# data_0 = data_0 * 255.0
data_0 = data_0.reshape(data_0.shape[0], 1)

poly3 = PolynomialFeatures(3)
featureSelection3 = poly3.fit_transform(data_0)
featureSelection3 = featureSelection3[:,1:3]
featureSelection3 = np.abs(featureSelection3)
max = np.max(featureSelection3)

featureSelection3 = featureSelection3[1200:1800, :]
# print featureSelection3.shape
feature_tmp = np.transpose(featureSelection3)

featureSelection3_new = []
for i in xrange(300):
    if featureSelection3_new == []:
        featureSelection3_new = featureSelection3
    else:
        featureSelection3_new = np.transpose(featureSelection3_new)
        featureSelection3_new = np.row_stack((featureSelection3_new, feature_tmp))
        featureSelection3_new = np.transpose(featureSelection3_new)

print featureSelection3_new.shape
print featureSelection3_new
featureSelection3_new = np.abs(featureSelection3_new)
# max = np.max(featureSelection3)
print max
featureSelection3_new = featureSelection3_new / np.float64(max)
featureSelection3_new = featureSelection3_new * 255.0
pl.imshow(featureSelection3_new, cmap='gray')
pl.show()
