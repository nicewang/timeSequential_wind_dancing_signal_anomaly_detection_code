from travel_path import *
from getSkews import *

path = "original_onePointData/"
files = travel_txt(path)
list_files(files)

for i in range(files.shape[0]):
    SpacePoint = ""
    if i == 0:
        SpacePoint = "0.1km"
    elif i == 1:
        SpacePoint = "10.1km"
    elif i == 2:
        SpacePoint = "10.6km"
    elif i == 3:
        SpacePoint = "11.1km"
    elif i == 4:
        SpacePoint = "11.6km"
    elif i == 5:
        SpacePoint = "12.1km"
    elif i == 6:
        SpacePoint = "12.6km"
    elif i == 7:
        SpacePoint = "3.1km"
    elif i == 8:
        SpacePoint = "3.6km"
    elif i == 9:
        SpacePoint = "4.1km"
    elif i == 10:
        SpacePoint = "4.6km"
    elif i == 11:
        SpacePoint = "5.1km"
    elif i == 12:
        SpacePoint = "5.6km"
    elif i == 13:
        SpacePoint = "6.1km"
    elif i == 14:
        SpacePoint = "6.6km"
    elif i == 15:
        SpacePoint = "7.1km"
    elif i == 16:
        SpacePoint = "7.6km"
    elif i == 17:
        SpacePoint = "8.1km"
    elif i == 18:
        SpacePoint = "8.6km"
    elif i == 19:
        SpacePoint = "9.1km"
    else:
        SpacePoint = "9.6km"
    skews = getSkews(files[i])
    np.savetxt(u"skews/Skews of Point at " + SpacePoint + u".txt", skews)

