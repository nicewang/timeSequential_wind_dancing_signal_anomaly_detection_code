import numpy as np

data = np.genfromtxt("Data_of_Point_at_3.6km.txt")
print(data.shape)

data_former = data[:864,:]
data_latter = data[864:,:]

print(data_former.shape)
print(data_latter.shape)
print(data_former)
print(data_latter)

np.savetxt("Data_of_Point_at_3.6km_Former.txt",data_former)
np.savetxt("Data_of_Point_at_3.6km_Latter.txt",data_latter)