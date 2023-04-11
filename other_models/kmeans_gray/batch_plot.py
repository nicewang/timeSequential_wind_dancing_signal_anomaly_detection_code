from travel_path import *
import pylab as pl

mark = ['ob', 'or', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']

files = travel_txt('cluster_freqXstd/')
files = files.reshape(20,1)
files1 = np.copy(files[6:16])
files2 = np.row_stack((files[16:],files[:6]))

xlines = np.genfromtxt('Mild Outlier.txt')
xlines = xlines.reshape(20,1)
xlines1 = np.copy(xlines[6:16])
xlines2 = np.row_stack((xlines[16:],xlines[:6]))

pl.figure(figsize=(10,18))
for i in range(files1.shape[0]):
    data = np.genfromtxt(files1[i,0])

    SpacePoint = files1[i,0].split(' ')[-1]
    SpacePoint = SpacePoint.split('.')[0] + '.' + SpacePoint.split('.')[1]
    print(SpacePoint)

    data_tmp = data[:,0]
    max = np.max(data_tmp, axis=0)
    min = np.min(data_tmp, axis=0)

    pl.subplot(5,2,i+1)
    for j in range(data.shape[0]):
        if data[j,2] == 1:
            pl.plot(data[j, 0], data[j, 1], mark[np.int(data[j, 2])], label='Relatively Abnormal Signal')
        else:
            pl.plot(data[j, 0], data[j, 1], mark[np.int(data[j, 2])])
    pl.legend()
    pl.xlabel("timeStd / V")
    pl.ylabel("freqCorr")
    pl.title("2-Clustering Result of freqXstd of Point at " + SpacePoint)

    # x = np.arange(min, max, (max-min)/data.shape[0])
    # if x.shape[0] > 1728:
    #     x = x[:1728]
    #
    # pl.axvline(xlines1[i], color='k', linewidth=0.5)
    # yline = 0.55*np.ones(data.shape[0])
    # pl.plot(x, yline, color='k', linewidth=0.5)
pl.tight_layout()
pl.savefig('cluster_freqXstd/fig1.png')

pl.figure(figsize=(10,18))
for i in range(files2.shape[0]):
    data = np.genfromtxt(files2[i,0])

    SpacePoint = files2[i,0].split(' ')[-1]
    SpacePoint = SpacePoint.split('.')[0] + '.' + SpacePoint.split('.')[1]
    print(SpacePoint)

    data_tmp = data[:,0]
    max = np.max(data_tmp, axis=0)
    min = np.min(data_tmp, axis=0)

    pl.subplot(5,2,i+1)
    for j in range(data.shape[0]):
        if data[j,2] == 1:
            pl.plot(data[j, 0], data[j, 1], mark[np.int(data[j, 2])], label='Relatively Abnormal Signal')
        else:
            pl.plot(data[j, 0], data[j, 1], mark[np.int(data[j, 2])])
    pl.legend()
    pl.xlabel("timeStd / V")
    pl.ylabel("freqCorr")
    pl.title("2-Clustering Result of freqXstd of Point at " + SpacePoint)

    # x = np.arange(min, max, (max-min)/data.shape[0])
    # if x.shape[0] > 1728:
    #     x = x[:1728]

    # pl.axvline(xlines2[i], color='k', linewidth=0.5)
    # yline = 0.55*np.ones(data.shape[0])
    # pl.plot(x, yline, color='k', linewidth=0.5)
pl.tight_layout()
pl.savefig('cluster_freqXstd/fig2.png')
