from skimage import transform
import numpy as np

w,h,c = 4,6,1

a = np.array([[[1],[2],[3]],
              [[4],[5],[6]]])
print(a.shape)
print(a)
b = transform.resize(a,(w,h,c))
print(b.shape)
print(b)