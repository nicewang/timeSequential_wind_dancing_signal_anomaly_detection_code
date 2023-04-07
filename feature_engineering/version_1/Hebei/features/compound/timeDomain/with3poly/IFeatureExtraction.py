import numpy as np
from sklearn.feature_extraction import image

path = "Compound-Features of Point at3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)

patches = image.extract_patches_2d(data, (2, 2), max_patches=2, random_state=0)
print patches.shape
