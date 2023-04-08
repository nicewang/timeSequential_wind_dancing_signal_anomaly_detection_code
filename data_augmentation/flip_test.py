import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.flip(a,axis=0)
c = np.flip(a,axis=1)
print(b)
print(c)

f = np.flip(b,axis=1)
print(f)

d = np.flip(f,axis=0)
e = np.flip(f,axis=1)
print(d)
print(e)

g = np.transpose(a)
g1 = np.flip(g, axis=0)
g2 = np.flip(g, axis=1)
g3 = np.flip(g2, axis=0)
g1 = np.transpose(g1)
g2 = np.transpose(g2)
g3 = np.transpose(g3)
print(g1)
print(g2)
print(g3)