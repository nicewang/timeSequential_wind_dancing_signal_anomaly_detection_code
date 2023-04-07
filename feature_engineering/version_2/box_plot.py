import numpy as np
import pandas as pd
import pylab as pl

data = np.genfromtxt("original_onePointData/Data_of_Point_at_3.1km.txt")
data = np.array(data)
data = np.diff(data)
print(data.shape)

data_new = []
for i in range(287):
    data1 = data[600*i:600*(i+1)]
    if data_new == []:
        data_new = data1
    else:
        data_new = np.column_stack((data_new,data1))

df = pd.DataFrame(data_new)
ret = df.boxplot()

ret1 = pl.boxplot(data_new)
# pl.show()
print(ret1)