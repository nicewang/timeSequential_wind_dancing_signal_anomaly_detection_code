import numpy as np

data = np.array([[[0],[1],[0]],[[0],[0],[1]]])
print(data.shape)
print(data)
label1 = np.zeros(data.shape + (1,))
for index, letter in np.ndenumerate(data):
    if letter:
        label1[index][ord(str(letter)) - ord('1')] = 1
print(label1.shape)
print(label1)