import numpy as np
import pylab as pl

pl.figure(figsize=(7,7))

data0 = np.genfromtxt("result0/rbf/result.txt")
data1 = np.genfromtxt("result1/rbf/result.txt")
data2 = np.genfromtxt("result2/rbf/result.txt")
data = np.row_stack((data0, data1, data2))
data = np.flip(data, axis=0)
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
ratio = np.array([1,2,21])

pl.plot(ratio,data_all/5184.0, color='m', marker='.', linewidth=0.7, label='Accuracy in All, RBF kernel')
pl.plot(ratio,data_abnormal/192.0, color='r', marker='.', linewidth=0.7, label='Accuracy in Abnormal, RBF kernel')
pl.plot(ratio,data_normal/4992.0, color='purple', marker='.', linewidth=0.7, label='Accuracy in Normal, RBF kernel')
# pl.legend()

data0 = np.genfromtxt("result0/2poly/result.txt")
data1 = np.genfromtxt("result1/2poly/result.txt")
data2 = np.genfromtxt("result2/2poly/result.txt")
data = np.row_stack((data0, data1, data2))
data = np.flip(data, axis=0)
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal

pl.plot(ratio,data_all/5184.0, color='y', marker='.', linewidth=0.7, label='Accuracy in All, 2nd Poly kernel')
pl.plot(ratio,data_abnormal/192.0, color='orange', marker='.', linewidth=0.7, label='Accuracy in Abnormal, 2nd Poly kernel')
pl.plot(ratio,data_normal/4992.0, color='brown', marker='.', linewidth=0.7, label='Accuracy in Normal, 2nd Poly kernel')
# pl.legend()

data0 = np.genfromtxt("result0/3poly/result.txt")
data1 = np.genfromtxt("result1/3poly/result.txt")
data2 = np.genfromtxt("result2/3poly/result.txt")
data = np.row_stack((data0, data1, data2))
data = np.flip(data, axis=0)
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.plot(ratio,data_all/5184.0, color='c', marker='.', linewidth=0.7, label='Accuracy in All, 3rd Poly kernel')
pl.plot(ratio,data_abnormal/192.0, color='b', marker='.', linewidth=0.7, label='Accuracy in Abnormal, 3rd Poly kernel')
pl.plot(ratio,data_normal/4992.0, color='k', marker='.', linewidth=0.7, label='Accuracy in Normal, 3rd Poly kernel')
pl.legend()

pl.xticks(ratio)
pl.xlabel("Ratio of Normal and Abnormal")
pl.ylabel("Test Accuracy Rate")
pl.title("Test Accuracy Rate in Test Set\n"
         + "with Different Normal and Abnormal Ratio in Training Set")

pl.tight_layout()

pl.savefig(u'result.png')
# pl.show()