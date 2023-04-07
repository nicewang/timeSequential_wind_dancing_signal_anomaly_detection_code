import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    path = '2017060613_CH01.txt'
    # data=pd.read_csv(path)
    k = 23493
    data = np.genfromtxt(path)
    data = np.array(data)
    print data.shape
