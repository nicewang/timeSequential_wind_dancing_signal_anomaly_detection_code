import numpy as np

a = np.array([[1,2,3,4,5,6,7,8],
              [11,12,13,14,15,16,17,18]])
print(a)
b = np.copy(a)
b = b.reshape(4,4)
print(b)
