import numpy as np

data = np.genfromtxt("training_fr_timeChroma/training data.txt")
label = np.genfromtxt("training_fr_timeChroma/labels.txt")

print(data.shape)
print(label.shape)

data_new = []
label_new = []
for i in range(label.shape[0]):
    if label[i] == 1:
        if data_new == []:
            data_new = data[i]
            data_new = data_new.reshape(60,)
        else:
            data_new = np.row_stack((data_new, data[i]))
print(data_new.shape)
np.savetxt("train_abnormal_set/data.txt", data_new)