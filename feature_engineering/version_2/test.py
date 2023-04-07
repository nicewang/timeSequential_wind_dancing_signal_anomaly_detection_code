import numpy as np

a = np.array([[1,2],[3,4]])
b = []
for i in range(2-1):
    for j in range(a.shape[0]):
        if b == []:
            b = a
            b = np.row_stack((b, a[j, :]))
        else:
            b = np.row_stack((b, a[j,:]))
c = []
for i in range(3-1):
    for j in range(a.shape[1]):
        if c == []:
            c = b
            c = np.column_stack((c, b[:, j]))
        else:
            c = np.column_stack((c, b[:,j]))
print(c.shape)
print(c)
