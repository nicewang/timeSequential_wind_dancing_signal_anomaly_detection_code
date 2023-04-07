import numpy as np
from sklearn.feature_selection import RFECV
from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data
y = iris.target
estimator = LinearSVC()
selector = RFECV(estimator=estimator,cv=3)
selector.fit(x,y)
selector.n_features_
selector.support_
selector.ranking_
selector.grid_scores_
