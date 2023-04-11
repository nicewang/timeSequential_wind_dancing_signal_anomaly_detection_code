from travel_path import *

freqCorr_files = travel_txt("freqCorr/")
timeStd_files = travel_txt("timeStd/")

for i in range(freqCorr_files.shape[0]):
    SpacePoint = freqCorr_files[i].split(' ')[-1]
    SpacePoint = SpacePoint.split('.')[0] + '.' + SpacePoint.split('.')[1] + '.' + SpacePoint.split('.')[-1]
    SpacePoint1 = timeStd_files[i].split('_')[-1]
    SpacePoint1 = SpacePoint1.split('.')[0] + '.' + SpacePoint1.split('.')[1] + '.' + SpacePoint.split('.')[-1]
    if SpacePoint == SpacePoint1:
        print("Bingo!")
    print(SpacePoint)

    data_freCorr = np.genfromtxt(freqCorr_files[i])
    data_timeStd = np.genfromtxt(timeStd_files[i])
    data_timeStd = np.transpose(data_timeStd)
    data_timeStd = data_timeStd.reshape(1728, )
    # Normalization
    data_timeStd = data_timeStd/np.max(data_timeStd)
    data_freqStd = np.column_stack((data_timeStd, data_freCorr))
    print(data_freqStd.shape)

    np.savetxt("freqStd/freqStd of point at " + SpacePoint, data_freqStd)
