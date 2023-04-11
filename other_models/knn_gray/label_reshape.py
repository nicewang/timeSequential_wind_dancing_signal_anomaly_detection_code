from travel_path import *

path = "labels-0.55/"
files = travel_txt(path)

for i in range(files.shape[0]):
    SpacePoint = files[i].split('/')[-1]
    SpacePoint = SpacePoint.split(' ')[-1]
    print(SpacePoint)

    data = np.genfromtxt(files[i])
    data_new = data[:1727]
    print(data_new.shape)
    np.savetxt(path + "labels of point at " + SpacePoint, data_new)
