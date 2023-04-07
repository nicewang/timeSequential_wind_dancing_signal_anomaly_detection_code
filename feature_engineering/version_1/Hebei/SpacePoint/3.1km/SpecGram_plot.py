import numpy as np
from matplotlib.pyplot import specgram
import matplotlib.pyplot as plt

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)

fs = data.shape[0]
fs = fs / (24*3600.0)

ret = specgram(data, Fs=fs, xextent=(0,24))

print ret

plt.colorbar()

plt.show()
