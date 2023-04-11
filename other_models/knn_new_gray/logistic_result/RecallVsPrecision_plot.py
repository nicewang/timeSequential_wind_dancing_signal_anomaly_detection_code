import numpy as np
import pylab as pl

pl.figure(figsize=(11.5,10))

data = np.genfromtxt("logistic_result0/liblinear/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))
k = np.array(['1.0', '100000.0', '1e+10', '1e+15', '1e+20'])

pl.subplot(321)
pl.plot(k,data_abnormal/192.0, color='blue', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,precision, color='orange', marker='.', linewidth=0.7, label='Normalized-Precision of Abnormal Recognition')
pl.xlabel("C")
pl.title("Test Accuracy Rate vs Test Normalized-Precision with Different C\n"
         + "(Ratio of Normal and Abnormal is 21:1 in Training Set)\n"
         + "('liblinear' Solver)")
pl.legend()

data = np.genfromtxt("logistic_result0/saga/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.subplot(322)
pl.plot(k,data_abnormal/192.0, color='purple', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,precision, color='green', marker='.', linewidth=0.7, label='Normalized-Precision of Abnormal Recognition')
pl.xlabel("C")
pl.title("Test Accuracy Rate vs Test Normalized-Precision with Different C\n"
         + "(Ratio of Normal and Abnormal is 21:1 in Training Set)\n"
         + "(SAGA Solver)")
pl.legend()

data = np.genfromtxt("logistic_result1/liblinear/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.subplot(323)
pl.plot(k,data_abnormal/192.0, color='blue', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,precision, color='orange', marker='.', linewidth=0.7, label='Normalized-Precision of Abnormal Recognition')
pl.xlabel("C")
pl.title("Test Accuracy Rate vs Test Normalized-Precision with Different C\n"
         + "(Ratio of Normal and Abnormal is 2:1 in Training Set)\n"
         + "('liblinear' Solver)")
pl.legend()

data = np.genfromtxt("logistic_result1/saga/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.subplot(324)
pl.plot(k,data_abnormal/192.0, color='purple', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,precision, color='green', marker='.', linewidth=0.7, label='Normalized-Precision of Abnormal Recognition')
pl.xlabel("C")
pl.title("Test Accuracy Rate vs Test Normalized-Precision with Different C\n"
         + "(Ratio of Normal and Abnormal is 2:1 in Training Set)\n"
         + "(SAGA Solver)")
pl.legend()

data = np.genfromtxt("logistic_result2/liblinear/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.subplot(325)
pl.plot(k,data_abnormal/192.0, color='blue', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,precision, color='orange', marker='.', linewidth=0.7, label='Normalized-Precision of Abnormal Recognition')
pl.xlabel("C")
pl.title("Test Accuracy Rate vs Test Normalized-Precision with Different C\n"
         + "(Ratio of Normal and Abnormal is 1:1 in Training Set)\n"
         + "('liblinear' Solver)")
pl.legend()

data = np.genfromtxt("logistic_result2/saga/result.txt")
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal
precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))

pl.subplot(326)
pl.plot(k,data_abnormal/192.0, color='purple', marker='.', linewidth=0.7, label='Test Accuracy Rate in Abnormal Signal')
pl.plot(k,precision, color='green', marker='.', linewidth=0.7, label='Normalized-Precision of Abnormal Recognition')
pl.xlabel("C")
pl.title("Test Accuracy Rate vs Test Normalized-Precision with Different C\n"
         + "(Ratio of Normal and Abnormal is 1:1 in Training Set)\n"
         + "(SAGA Solver)")
pl.legend()

pl.tight_layout()

pl.savefig(u'recall_precision_result.png')
