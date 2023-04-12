from travel_path import *

path = 'labeledTimeFreq/train_set/'
files = travel_txt(path)

data = []
labels = []
for i in range(files.shape[0]):
    data_tmp = np.genfromtxt(files[i])
    data_tmp1 = data_tmp[:250,:]
    for j in range(data_tmp1.shape[1]):
        data_tmp2 = data_tmp1[:,j]
        data_tmp2 = data_tmp2.reshape(250,)

        # b = []
        # for ia in range(8 - 1):
        #     for ja in range(data_tmp2.shape[0]):
        #         if b == []:
        #             b = data_tmp2
        #             b = np.row_stack((b, data_tmp2[ja, :]))
        #         else:
        #             b = np.row_stack((b, data_tmp2[ja, :]))
        # c = []
        # for ia in range(8 - 1):
        #     for ja in range(data_tmp2.shape[1]):
        #         if c == []:
        #             c = b
        #             c = np.column_stack((c, b[:, ja]))
        #         else:
        #             c = np.column_stack((c, b[:, ja]))

        # b = np.zeros((5, 50, 1))
        # for i1 in range(5):
        #     for j1 in range(50):
        #         b[i1, j1, 0] = data_tmp2[i1, j1]
                # b[i1, j1, 1] = data_tmp2[i1, j1]
                # b[i1, j1, 2] = data_tmp2[i1, j1]
        # img = transform.resize(b,(10,24,1))
        # img = b

        # d = np.zeros((40, 96, 3))
        # for i1 in range(40):
        #     for j1 in range(96):
        #         d[i1, j1, 0] = c[i1, j1]
        #         d[i1, j1, 1] = c[i1, j1]
        #         d[i1, j1, 2] = c[i1, j1]
        # img = transform.resize(d, (40, 96, 3))
        data.append(data_tmp2)
    label_tmp1 = data_tmp[250,:]
    label_tmp1 = label_tmp1.reshape(1,label_tmp1.shape[0])
    # if data == []:
    #     data = data_tmp1
    # else:
    #     data = np.column_stack((data, data_tmp1))
    if labels == []:
        labels = label_tmp1
    else:
        labels = np.column_stack((labels, label_tmp1))
data = np.array(data)
labels = np.array(labels)
labels = labels.reshape(labels.shape[0]*labels.shape[1],)
print(data.shape)
print(labels.shape)
np.savetxt(u'training_fr_timeFreq/training data.txt', data)
np.savetxt(u'training_fr_timeFreq/labels.txt', labels)