import numpy as np

path_label_in = 'timeStd/labels/mild_outliers/labels of point at 3.6km.txt'
path_freqCorr = 'freqCorr/freq corr of point at 3.6km.txt'

data_label_in = np.genfromtxt(path_label_in)
data_freqCorr = np.genfromtxt(path_freqCorr)

data_label_out = np.zeros(data_label_in.shape[0])
count = 0
for i in range(data_label_in.shape[0]):
    if data_label_in[i] == 1:
        count = count + 1
        if data_freqCorr[i] > 0.55:
            data_label_out[i] = 1
print(count)

# checking
count1 = 0
for i in range(data_label_out.shape[0]):
    if data_label_out[i] == 1:
        count1 = count1 + 1
print(count1)

# np.savetxt('labels-0.55/mild_outliers/labels of point at 3.6km.txt',data_label_out)

# data_label_out = np.zeros(1728)
# # checking
# count1 = 0
# for i in range(data_label_out.shape[0]):
#     if data_label_out[i] == 1:
#         count1 = count1 + 1
# print(count1)
# np.savetxt('labels/labels of point at 0.1km.txt',data_label_out)
