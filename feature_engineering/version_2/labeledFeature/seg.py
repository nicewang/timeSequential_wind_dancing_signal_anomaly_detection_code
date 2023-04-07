import numpy as np

data = np.genfromtxt('Labeled Feature of Point at 0.1km.txt')
print(data.shape)

data_former = data[:,:864]
data_latter = data[:,864:]

print(data_former.shape)
print(data_latter.shape)
print(data_former)
print(data_latter)

np.savetxt('Labeled Feature of Point at 0.1km Former.txt',data_former)
np.savetxt('Labeled Feature of Point at 0.1km Latter.txt',data_latter)