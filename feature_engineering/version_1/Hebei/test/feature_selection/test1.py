# -*- coding: utf-8 -*-
# 单变量特征选择
from sklearn.feature_selection import SelectKBest, f_classif

x = [[1,2,3,4,5],
     [5,4,3,2,1],
     [3,3,3,3,3],
     [1,1,1,1,1]]
y = [0,1,0,1]
selector = SelectKBest(score_func=f_classif, k=3) # 选择3个特征，指标使用的是方差分析F值
selector.fit(x,y)
selector.scores_ # 每一个特征的得分
selector.pvalues_
selector.get_support(True)  # 如果为True，则返回被选出的特征下标，
                            # 如果选择False，则返回的是一个布尔值组成的数组，该数组指示哪些特征被选择
selector.transform(x)
