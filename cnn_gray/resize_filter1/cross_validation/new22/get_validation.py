import numpy as np

data = np.genfromtxt("training_fr_timeChroma_new_1/training data.txt")
label = np.genfromtxt("training_fr_timeChroma_new_1/labels.txt")

print(data.shape)
print(label.shape)

data_tmp1 = data[864*5:864*7]
data_tmp1 = data_tmp1.reshape(1728,60)
data_tmp2 = data[1728*10:1728*11]
data_tmp2 = data_tmp2.reshape(1728,60)
data_tmp3 = data[1728*17:1728*18]
data_tmp3 = data_tmp3.reshape(1728,60)
data_new = np.row_stack((data_tmp1,data_tmp2,data_tmp3))

label_tmp1 = label[864*5:864*7]
label_tmp1 = label_tmp1.reshape(1728,1)
label_tmp2 = label[1728*10:1728*11]
label_tmp2 = label_tmp2.reshape(1728,1)
label_tmp3 = label[1728*17:1728*18]
label_tmp3 = label_tmp3.reshape(1728,1)
label_new = np.row_stack((label_tmp1,label_tmp2,label_tmp3))

print(data_new.shape, label_new.shape)

count = 0
for i in range(label_new.shape[0]):
    if label_new[i] == 1:
        count = count + 1
print(count)

np.savetxt("validate_set/training data.txt", data_new)
np.savetxt("validate_set/labels.txt", label_new)

data_tmp1 = data[:864*5]
data_tmp2 = data[864*7:1728*10]
data_tmp3 = data[1728*11:1728*17]
data_tmp4 = data[1728*18:]
data_new = np.row_stack((data_tmp1,data_tmp2,data_tmp3,data_tmp4))

label_tmp1 = label[:864*5]
label_tmp1 = label_tmp1.reshape(label_tmp1.shape[0],1)
label_tmp2 = label[864*7:1728*10]
label_tmp2 = label_tmp2.reshape(label_tmp2.shape[0],1)
label_tmp3 = label[1728*11:1728*17]
label_tmp3 = label_tmp3.reshape(label_tmp3.shape[0],1)
label_tmp4 = label[1728*18:]
label_tmp4 = label_tmp4.reshape(label_tmp4.shape[0],1)
label_new = np.row_stack((label_tmp1,label_tmp2,label_tmp3,label_tmp4))

print(data_new.shape, label_new.shape)

count = 0
for i in range(label_new.shape[0]):
    if label_new[i] == 1:
        count = count + 1
print(count)

np.savetxt("train_set/training data.txt", data_new)
np.savetxt("train_set/labels.txt", label_new)