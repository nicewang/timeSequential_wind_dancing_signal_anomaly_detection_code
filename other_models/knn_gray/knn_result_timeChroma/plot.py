import numpy as np
import pylab as pl

pl.figure(figsize=(5,10))

data = np.genfromtxt("knn_result0/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
k = np.array([1,2,3,4,5,6,7,8,9,10,
     11,12,13,14,15,16,17,
     18,19,20])

pl.subplot(311)
pl.plot(k,data_all/5184.0, color='k', marker='.', linewidth=0.7, label='Test Accuracy Rate in All Signal')
pl.plot(k,data_abnormal/192.0, color='m', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,data_normal/4992.0, color='c', marker='.', linewidth=0.7, label='Test Accuracy Rate in Normal Signal')
pl.xlabel("k")
pl.xticks(k)
pl.ylabel("Test Accuracy Rate")
pl.title("Test Accuracy Rate in Test Set with Different k\n"
         + "(Ratio of Normal and Abnormal is 21:1 in Training Set)")
pl.legend()

data = np.genfromtxt("knn_result1/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal

pl.subplot(312)
pl.plot(k,data_all/5184.0, color='k', marker='.', linewidth=0.7, label='Test Accuracy Rate in All Signal')
pl.plot(k,data_abnormal/192.0, color='m', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,data_normal/4992.0, color='c', marker='.', linewidth=0.7, label='Test Accuracy Rate in Normal Signal')
pl.xlabel("k")
pl.xticks(k)
pl.ylabel("Test Accuracy Rate")
pl.title("Test Accuracy Rate in Test Set with Different k\n"
         + "(Ratio of Normal and Abnormal is 2:1 in Training Set)")
pl.legend()

data = np.genfromtxt("knn_result2/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal

pl.subplot(313)
pl.plot(k,data_all/5184.0, color='k', marker='.', linewidth=0.7, label='Test Accuracy Rate in All Signal')
pl.plot(k,data_abnormal/192.0, color='m', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,data_normal/4992.0, color='c', marker='.', linewidth=0.7, label='Test Accuracy Rate in Normal Signal')
pl.xlabel("k")
pl.xticks(k)
pl.ylabel("Test Accuracy Rate")
pl.title("Test Accuracy Rate in Test Set with Different k\n"
         + "(Ratio of Normal and Abnormal is 1:1 in Training Set)")
pl.legend()

pl.tight_layout()

pl.savefig(u'result.png')
