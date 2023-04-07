from travel_path import *
from skimage import transform

path = 'train_set/'
files = travel_txt(path)

data = []
labels = []
for i in range(files.shape[0]):
    data_tmp = np.genfromtxt(files[i])
    data_tmp1 = data_tmp[:60,:]
    for j in range(data_tmp1.shape[1]):
        data_tmp2 = data_tmp1[:,j]
        data_tmp2 = data_tmp2.reshape(5, 12)
        b = np.zeros((5, 12, 3))
        for i1 in range(5):
            for j1 in range(12):
                b[i1, j1, 0] = data_tmp2[i1, j1]
                b[i1, j1, 1] = data_tmp2[i1, j1]
                b[i1, j1, 2] = data_tmp2[i1, j1]
        img = transform.resize(b,(100,100,3))
        data.append(img)
    label_tmp1 = data_tmp[60,:]
    label_tmp1 = label_tmp1.reshape(1,label_tmp1.shape[0])
    # if data == []:
    #     data = data_tmp1
    # else:
    #     data = np.column_stack((data, data_tmp1))
    if labels == []:
        labels = label_tmp1
    else:
        labels = np.column_stack((labels, label_tmp1))

data = np.asarray(data,np.float32)
labels = labels.reshape(labels.shape[0]*labels.shape[1],)
print(data.shape)
print(labels.shape)

# data_tmp = np.genfromtxt(files[0])
# data_tmp1 = data_tmp[:60,:]
# print(data_tmp1.shape)
# data_tmp2 = data_tmp1[:,0]
# print(data_tmp2.shape)
# data_tmp2 = data_tmp2.reshape(5,12)
# print(data_tmp2.shape)
