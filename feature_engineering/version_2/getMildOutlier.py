from travel_path import *

path = 'timeStd/'
files = travel_txt(path)
data_new = []
for i in range(files.shape[0]):
    print(files[i])

    data = np.genfromtxt(files[i])
    data = np.transpose(data)
    data = data.reshape(72 * 24, )

    up = np.percentile(data, 75)
    down = np.percentile(data, 25)
    IQR = up - down
    mildOutlier = up + IQR*1.5
    if data_new == []:
        data_new = mildOutlier
    else:
        data_new = np.row_stack((data_new, mildOutlier))
np.savetxt('Mild Outlier.txt', data_new)