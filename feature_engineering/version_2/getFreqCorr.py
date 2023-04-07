from travel_path import *

path = "freq_models/"
files = travel_txt(path)

data_path = "original_onePointData/"
data_files = travel_txt(data_path)
list_files(data_files)

for i in range(1, data_files.shape[0]):
    if i == 1:
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

    data = np.genfromtxt(data_files[i])
    data = np.array(data)
    data = np.diff(data)

    corr_data = []
    for j in range(1728):
        if j < 6:
            sub_data = data[:1200]
        elif j > 1721:
            sub_data = data[171592:]
        else:
            sub_data = data[100 * j - 550:100 * (j + 1) + 550]

        # 进行快速傅立叶变换
        xf1 = np.fft.rfft(sub_data)
        xf1 = np.abs(xf1)
        xf1 = xf1 / max(xf1)

        corr = -1
        for k in range(6):
            xf = np.genfromtxt(files[k])
            tmp_corr = np.corrcoef(np.array([xf1, xf]))
            tmp_corr = tmp_corr[0, 1]
            if tmp_corr > corr:
                corr = tmp_corr

        if corr_data == []:
            corr_data = corr
        else:
            corr_data = np.row_stack([corr_data, corr])

    print(i)
    print(corr_data.shape)
    print(corr_data)
    np.savetxt(u'freqCorr/freq corr of point at ' + SpacePoint + u'.txt', corr_data)
