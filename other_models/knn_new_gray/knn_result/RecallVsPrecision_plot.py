import numpy as np
import pylab as pl

pl.figure(figsize=(5.5,10))

data = np.genfromtxt("knn_result0/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))
k = np.array([1,2,3,4,5,6,7,8,9,10,
     11,12,13,14,15,16,17,
     18,19,20])

pl.subplot(311)
pl.plot(k,data_abnormal/192.0, color='red', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,precision, color='purple', marker='.', linewidth=0.7, label='Normalized-Precision of Abnormal Recognition')
pl.xlabel("k")
pl.xticks(k)
pl.title("Test Accuracy Rate vs Test Normalized-Precision with Different k\n"
         + "(Ratio of Normal and Abnormal is 21:1 in Training Set)")
pl.legend()

data = np.genfromtxt("knn_result1/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.subplot(312)
pl.plot(k,data_abnormal/192.0, color='red', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,precision, color='purple', marker='.', linewidth=0.7, label='Normalized-Precision of Abnormal Recognition')
pl.xlabel("k")
pl.xticks(k)
pl.title("Test Accuracy Rate vs Test Normalized-Precision with Different k\n"
         + "(Ratio of Normal and Abnormal is 2:1 in Training Set)")
pl.legend()

data = np.genfromtxt("knn_result2/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.subplot(313)
pl.plot(k,data_abnormal/192.0, color='red', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,precision, color='purple', marker='.', linewidth=0.7, label='Normalized-Precision of Abnormal Recognition')
pl.xlabel("k")
pl.xticks(k)
pl.title("Test Accuracy Rate vs Test Normalized-Precision with Different k\n"
         + "(Ratio of Normal and Abnormal is 1:1 in Training Set)")
pl.legend()

pl.tight_layout()

pl.savefig(u'recall_precision_result.png')
