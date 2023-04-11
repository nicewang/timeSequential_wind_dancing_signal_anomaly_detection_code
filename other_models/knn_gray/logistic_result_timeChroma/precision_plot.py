import numpy as np
import pylab as pl

pl.figure(figsize=(6.5,7.2))

data = np.genfromtxt("logistic_result0/liblinear/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))
k = np.array(['1.0', '100000.0', '1e+10', '1e+15', '1e+20'])

pl.plot(k,precision, color='blue', marker='.', linewidth=0.7, label='Normal:Abnormal=21:1 in Training Set, LibLinear')
pl.legend()

data = np.genfromtxt("logistic_result0/saga/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.plot(k,precision, color='blue', marker='.', linewidth=0.7, label='Normal:Abnormal=21:1 in Training Set, SAGA',
        linestyle="--")
pl.legend()

data = np.genfromtxt("logistic_result1/liblinear/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.plot(k,precision, color='purple', marker='.', linewidth=0.7, label='Normal:Abnormal=2:1 in Training Set, LibLinear')
pl.legend()

data = np.genfromtxt("logistic_result1/saga/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.plot(k,precision, color='purple', marker='.', linewidth=0.7, label='Normal:Abnormal=2:1 in Training Set, SAGA',
        linestyle="--")
pl.legend()

data = np.genfromtxt("logistic_result2/liblinear/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.plot(k,precision, color='brown', marker='.', linewidth=0.7, label='Normal:Abnormal=1:1 in Training Set, LibLinear')
pl.legend()

data = np.genfromtxt("logistic_result2/saga/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.plot(k,precision, color='brown', marker='.', linewidth=0.7, label='Normal:Abnormal=1:1 in Training Set, SAGA',
        linestyle="--")
pl.legend()

pl.xlabel("C")
# pl.xticks(k)
pl.ylabel("Normalized-Precision of Abnormal Recognition")
pl.title("Test Normalized-Precision of Abnormal Recognition with Different C")

pl.tight_layout()

pl.savefig(u'precision_result.png')
