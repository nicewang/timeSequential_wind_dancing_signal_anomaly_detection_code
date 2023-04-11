import numpy as np
import pylab as pl

pl.figure(figsize=(6,6))

data0 = np.genfromtxt("result0/rbf/result.txt")
data1 = np.genfromtxt("result1/rbf/result.txt")
data2 = np.genfromtxt("result2/rbf/result.txt")
data = np.row_stack((data0, data1, data2))
data = np.flip(data, axis=0)
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))
ratio = np.array([1,2,21])

pl.plot(ratio,data_abnormal/192.0, color='r', marker='.', linewidth=0.7, label='Accuracy in Abnormal, RBF kernel')
pl.plot(ratio,precision, color='purple', marker='.', linewidth=0.7, label='Normalized-Precision in Abnormal, RBF kernel')
# pl.legend()

data0 = np.genfromtxt("result0/2poly/result.txt")
data1 = np.genfromtxt("result1/2poly/result.txt")
data2 = np.genfromtxt("result2/2poly/result.txt")
data = np.row_stack((data0, data1, data2))
data = np.flip(data, axis=0)
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.plot(ratio,data_abnormal/192.0, color='orange', marker='.', linewidth=0.7, label='Accuracy in Abnormal, 2nd Poly kernel')
pl.plot(ratio,precision, color='b', marker='.', linewidth=0.7, label='Normalized-Precision in Abnormal, 2nd Poly kernel')
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

pl.plot(ratio,data_abnormal/192.0, color='brown', marker='.', linewidth=0.7, label='Accuracy in Abnormal, 3rd Poly kernel')
pl.plot(ratio,precision, color='green', marker='.', linewidth=0.7, label='Normalized-Precision in Abnormal, 3rd Poly kernel')
pl.legend()

pl.xticks(ratio)
pl.xlabel("Ratio of Normal and Abnormal")
pl.title("Test Accuracy Rate vs Test Normalized-Precision\n"
         + "with Different Normal and Abnormal Ratio in Training Set")

pl.tight_layout()

pl.savefig(u'recall_precision_result.png')
# pl.show()
