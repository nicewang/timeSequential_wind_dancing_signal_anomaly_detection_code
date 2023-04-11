import numpy as np
import pylab as pl

data = np.genfromtxt("knn_result0/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))
k = np.array([1,2,3,4,5,6,7,8,9,10,
     11,12,13,14,15,16,17,
     18,19,20])

pl.plot(k,precision, color='blue', marker='.', linewidth=0.7, label='Normal:Abnormal=21:1 in Training Set')

data = np.genfromtxt("knn_result1/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.plot(k,precision, color='purple', marker='.', linewidth=0.7, label='Normal:Abnormal=2:1 in Training Set')

data = np.genfromtxt("knn_result2/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.plot(k,precision, color='brown', marker='.', linewidth=0.7, label='Normal:Abnormal=1:1 in Training Set')

pl.xlabel("k")
pl.xticks(k)
pl.ylabel("Normalized-Precision of Abnormal Recognition")
pl.title("Test Normalized-Precision of Abnormal Recognition with Different k")
pl.legend()

pl.tight_layout()

pl.savefig(u'precision_result.png')
