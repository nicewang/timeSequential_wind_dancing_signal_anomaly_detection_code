# -*- coding: utf-8 -*-
# 注意：特征提取对于预测性能的提升没有必然的联系，接下来进行比较；
from sklearn.feature_selection import RFE
from sklearn.svm import LinearSVC
from sklearn import cross_validation
from sklearn.datasets import load_iris

# 加载数据
iris = load_iris()
X = iris.data
y = iris.target
# 特征提取
estimator = LinearSVC()
selector = RFE(estimator=estimator, n_features_to_select=2)
X_t = selector.fit_transform(X,y)
# 切分测试集与验证集
x_train,x_test,y_train,y_test = cross_validation.train_test_split(X,y,
                                    test_size=0.25,random_state=0,stratify=y)
x_train_t,x_test_t,y_train_t,y_test_t = cross_validation.train_test_split(X_t,y,
                                    test_size=0.25,random_state=0,stratify=y)

clf = LinearSVC()
clf_t = LinearSVC()
clf.fit(x_train,y_train)
clf_t.fit(x_train_t,y_train_t)
print 'original dataset getFront score:',clf.score(x_test,y_test)
print 'selected dataset getFront score:',clf_t.score(x_test_t,y_test_t)
