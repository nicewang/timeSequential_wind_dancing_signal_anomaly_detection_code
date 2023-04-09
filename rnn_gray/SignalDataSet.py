from travel_path import *

def getDataLabel(path):
    files = travel_txt(path)
    data = []
    label = []
    for i in range(files.shape[0]):
        data.append([])
        label.append([])
        data_tmp = np.genfromtxt(files[i])
        count = 0
        for j in range(data_tmp.shape[1]):
            data_tmp1 = data_tmp[:60, j]
            data_tmp1 = data_tmp1.reshape(5, 12)
            label_tmp1 = data_tmp[60:, j]
            if count == 24:
                count = 0
                data.append([])
                label.append([])
            data[-1].append(data_tmp1)
            label[-1].append(label_tmp1)
            count = count + 1
    data = np.array(data)
    label = np.array(label)
    # print(data.shape)
    # print(label.shape)
    return data, label

# validation
# path = 'train_set_new/'
# data, label = getDataLabel(path)
# print(data.shape)
# print(label.shape)
