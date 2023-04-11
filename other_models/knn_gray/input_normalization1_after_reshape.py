from travel_path import *

path = "original_onePointData/"
files = travel_txt(path)

for i in range(files.shape[0]):
    SpacePoint = files[i].split('/')[-1]
    SpacePoint = SpacePoint.split('_')[-1]
    print(SpacePoint)

    data = np.genfromtxt(files[i])
    data_new = []
    for j in range(1727):
        data_tmp = data[j,:]
        max = np.max(abs(data_tmp),axis=0)
        data_tmp = data_tmp / max
        if data_new == []:
            data_new = data_tmp
        else:
            data_new = np.row_stack((data_new, data_tmp))
    print(data_new.shape)
    np.savetxt("original_onePointData_normalization1/Data_of_Point_at_" + SpacePoint, data_new)
