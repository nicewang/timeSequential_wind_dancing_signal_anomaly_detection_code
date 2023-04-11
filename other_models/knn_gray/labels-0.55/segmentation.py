import numpy as np

data = np.genfromtxt("labels of point at 3.6km.txt")
print(data.shape)

data_former = data[:864]
data_latter = data[864:]

print(data_former.shape)
print(data_latter.shape)
print(data_former)
print(data_latter)

np.savetxt("labels of point at 3.6km former.txt",data_former)
np.savetxt("labels of point at 3.6km latter.txt",data_latter)