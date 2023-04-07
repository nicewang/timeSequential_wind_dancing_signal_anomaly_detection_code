import numpy as np

path = "Data_of_Point_at_0.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)

for i in np.arange(24):
    if i == 23:
        data_sub = data[7200*i:]
    else:
        data_sub = data[7200*i:7200*(i+1)]
    np.savetxt("timeSeg/"+str(i)+"-"+str(i+1)+".txt", data_sub)
