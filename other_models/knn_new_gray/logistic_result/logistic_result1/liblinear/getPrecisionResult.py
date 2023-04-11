import numpy as np

data = np.genfromtxt('result.txt')
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal

precision = (data_abnormal*(4992.0/192.0))/(data_abnormal*(4992.0/192.0)+(4992-data_normal))
print(precision)
np.savetxt("precision.txt",precision)