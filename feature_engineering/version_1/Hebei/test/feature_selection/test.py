# -*- coding: utf-8 -*-
# 过滤式特征选择
# 根据方差进行选择，方差越小，代表该属性识别能力很差，可以剔除
from sklearn.feature_selection import VarianceThreshold

x = [[100,1,2,3],
     [100,4,5,6],
     [100,7,8,9],
     [101,11,12,13]]
selector = VarianceThreshold(1)  #方差阈值值，
selector.fit(x)
selector.variances_    # 展现属性的方差
selector.transform(x)  # 进行特征选择
selector.get_support(True)  # 选择结果后，特征之前的索引
selector.inverse_transform(selector.transform(x))  # 将特征选择后的结果还原成原始数据
                                                   # 被剔除掉的数据，显示为0
