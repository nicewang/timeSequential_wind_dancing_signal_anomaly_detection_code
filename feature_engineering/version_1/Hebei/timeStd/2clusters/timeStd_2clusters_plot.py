import  numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

data = np.genfromtxt('timeStd_2clusters_23_24.txt')
data = np.array(data)

i = np.arange(23.0, 24.0, 1.0/72.0)
j = np.arange(0, 30000, 2)
i, j = np.meshgrid(j, i)

sc = plt.scatter(i, j, c=data, vmin=0, vmax=1, cmap=cm.coolwarm)
plt.colorbar(sc)

plt.xlabel('Space / m')
plt.ylabel('Time / h')
plt.title('2Clusters-Result Between 23 and 24')

plt.show()
