import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a * 2
c = a * 3

a = a.reshape(1,a.shape[0],a.shape[1])
b = b.reshape(1,b.shape[0],b.shape[1])
c = c.reshape(1,c.shape[0],c.shape[1])

d = np.row_stack((a, b, c))
print(d.shape)
print(d)

e = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
e = e.reshape(2,2,3)
print(e)
e1 = e[0]
print(e1)
e2 = e1
e2 = e2.reshape(6,)
print(e2)
f = e
f = f.reshape(2,6)
print(f)

a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.array([[8,8,9],[11,11,12]])
a3 = (a1 + a2) / 2.0
print(a3)
a4 = a3.reshape(1,6)
print(a4)

a0 = np.row_stack(([[1,2]],[[2,3]],[[3,4]]))
print(a0)
a11 = np.row_stack((a0,[[1,2]],[[2,3]],[[3,4]]))
print(a11)
a11 = np.row_stack((a11,[[1,2]],[[2,3]],[[3,4]]))
print(a11)
a00 = np.array([[2,3],[4,5],[6,7],[8,9],[10,11]])
a11 = np.row_stack((a11,a00))
print(a11)