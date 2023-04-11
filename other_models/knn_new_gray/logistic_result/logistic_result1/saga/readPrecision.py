import numpy as np

data = np.genfromtxt("precision.txt")
print(data.shape)
for i in range(data.shape[0]):
    print(data[i])
