import numpy as np

data = np.genfromtxt("training data.txt")
print(data.shape)
labels = np.genfromtxt("labels.txt")

count = 0
for i in range(labels.shape[0]):
    if labels[i] == 1:
        count = count + 1
print(count)