import numpy as np
import pylab as pl

pl.figure(figsize=(10,10))

data = np.genfromtxt("logistic_result0/liblinear/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
C = np.array(['1.0', '100000.0', '1e+10', '1e+15', '1e+20'])

pl.subplot(321)
pl.plot(C,data_all/5184.0, color='k', marker='.', linewidth=0.7, label='Test Accuracy Rate in All Signal')
pl.plot(C,data_abnormal/192.0, color='r', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(C,data_normal/4992.0, color='b', marker='.', linewidth=0.7, label='Test Accuracy Rate in Normal Signal')
pl.xlabel("C")
# pl.xticks(C)
pl.ylabel("Test Accuracy Rate")
pl.title("Test Accuracy Rate in Test Set with Different C\n"
         + "(Ratio of Normal and Abnormal is 21:1 in Training Set)\n"
         + "('liblinear' Solver)")
pl.legend()

data = np.genfromtxt("logistic_result0/saga/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal

pl.subplot(322)
pl.plot(C,data_all/5184.0, color='k', marker='.', linewidth=0.7, label='Test Accuracy Rate in All Signal')
pl.plot(C,data_abnormal/192.0, color='m', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(C,data_normal/4992.0, color='c', marker='.', linewidth=0.7, label='Test Accuracy Rate in Normal Signal')
pl.xlabel("C")
# pl.xticks(C)
pl.ylabel("Test Accuracy Rate")
pl.title("Test Accuracy Rate in Test Set with Different C\n"
         + "(Ratio of Normal and Abnormal is 21:1 in Training Set)\n"
         + "(SAGA Solver)")
pl.legend()

data = np.genfromtxt("logistic_result1/liblinear/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal

pl.subplot(323)
pl.plot(C,data_all/5184.0, color='k', marker='.', linewidth=0.7, label='Test Accuracy Rate in All Signal')
pl.plot(C,data_abnormal/192.0, color='r', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(C,data_normal/4992.0, color='b', marker='.', linewidth=0.7, label='Test Accuracy Rate in Normal Signal')
pl.xlabel("C")
# pl.xticks(C)
pl.ylabel("Test Accuracy Rate")
pl.title("Test Accuracy Rate in Test Set with Different C\n"
         + "(Ratio of Normal and Abnormal is 2:1 in Training Set)\n"
         + "('liblinear' Solver)")
pl.legend()

data = np.genfromtxt("logistic_result1/saga/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal

pl.subplot(324)
pl.plot(C,data_all/5184.0, color='k', marker='.', linewidth=0.7, label='Test Accuracy Rate in All Signal')
pl.plot(C,data_abnormal/192.0, color='m', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(C,data_normal/4992.0, color='c', marker='.', linewidth=0.7, label='Test Accuracy Rate in Normal Signal')
pl.xlabel("C")
# pl.xticks(C)
pl.ylabel("Test Accuracy Rate")
pl.title("Test Accuracy Rate in Test Set with Different C\n"
         + "(Ratio of Normal and Abnormal is 2:1 in Training Set)\n"
         + "(SAGA Solver)")
pl.legend()

data = np.genfromtxt("logistic_result2/liblinear/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal

pl.subplot(325)
pl.plot(C,data_all/5184.0, color='k', marker='.', linewidth=0.7, label='Test Accuracy Rate in All Signal')
pl.plot(C,data_abnormal/192.0, color='r', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(C,data_normal/4992.0, color='b', marker='.', linewidth=0.7, label='Test Accuracy Rate in Normal Signal')
pl.xlabel("C")
# pl.xticks(C)
pl.ylabel("Test Accuracy Rate")
pl.title("Test Accuracy Rate in Test Set with Different C\n"
         + "(Ratio of Normal and Abnormal is 1:1 in Training Set)\n"
         + "('liblinear' Solver)")
pl.legend()

data = np.genfromtxt("logistic_result2/saga/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal

pl.subplot(326)
pl.plot(C,data_all/5184.0, color='k', marker='.', linewidth=0.7, label='Test Accuracy Rate in All Signal')
pl.plot(C,data_abnormal/192.0, color='m', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(C,data_normal/4992.0, color='c', marker='.', linewidth=0.7, label='Test Accuracy Rate in Normal Signal')
pl.xlabel("C")
# pl.xticks(C)
pl.ylabel("Test Accuracy Rate")
pl.title("Test Accuracy Rate in Test Set with Different C\n"
         + "(Ratio of Normal and Abnormal is 1:1 in Training Set)\n"
         + "(SAGA Solver)")
pl.legend()

pl.tight_layout()

pl.savefig(u'result.png')
# pl.show()