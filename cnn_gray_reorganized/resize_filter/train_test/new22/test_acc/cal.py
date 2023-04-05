import numpy as np

data0 = np.genfromtxt('count_abnormal.txt')
data = np.copy(data0)
data = data * (5184.0-192.0)/192.0
data1 = np.genfromtxt('count.txt')
data_normal = (5184.0-192.0)*np.ones(data.shape[0])
data_new = data/(data+(data_normal-(data1-data0)))
print(data_new[11])
print(data_new[16])
print(data_new[17])