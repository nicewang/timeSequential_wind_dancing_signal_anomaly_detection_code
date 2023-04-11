import numpy as np

data = np.genfromtxt('result.txt')
data_abnormal = data[:,0]
data_all = data[:,1]
data_normal = data_all - data_abnormal

for i in range(data.shape[0]):
    print(data_all[i]/5184.0,data_normal[i]/4992.0,data_abnormal[i]/192.0)