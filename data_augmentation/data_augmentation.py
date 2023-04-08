# -*- coding: utf-8 -*-
import numpy as np

data = np.genfromtxt("training_fr_timeChroma/training data.txt")
# print(data.shape)
labels = np.genfromtxt("training_fr_timeChroma/labels.txt")

data_origin = []
data_flip_a = []
data_flip_b = []
data_flip_c = []
abnormal_count = 0
for i in range(labels.shape[0]):
    if labels[i] == 1:
        data_tmp = data[i,:]
        data_tmp = data_tmp.reshape(5,12)
        data_tmp_a = np.flip(data_tmp, axis=0)
        data_tmp_b = np.flip(data_tmp, axis=1)
        data_tmp_c = np.flip(data_tmp_b, axis=0)
        data_tmp = data_tmp.reshape(1,5,12)
        data_tmp_a = data_tmp_a.reshape(1, 5, 12)
        data_tmp_b = data_tmp_b.reshape(1, 5, 12)
        data_tmp_c = data_tmp_c.reshape(1, 5, 12)
        if data_origin == []:
            data_origin = data_tmp
            data_flip_a = data_tmp_a
            data_flip_b = data_tmp_b
            data_flip_c = data_tmp_c
        else:
            data_origin = np.row_stack((data_origin, data_tmp))
            data_flip_a = np.row_stack((data_flip_a, data_tmp_a))
            data_flip_b = np.row_stack((data_flip_b, data_tmp_b))
            data_flip_c = np.row_stack((data_flip_c, data_tmp_c))
        abnormal_count = abnormal_count + 1

# 打乱顺序
# print(abnormal_count)
arr0 = np.arange(abnormal_count)
arr1 = np.arange(abnormal_count)
arr2 = np.arange(abnormal_count)
arr3 = np.arange(abnormal_count)
np.random.shuffle(arr0)
np.random.shuffle(arr1)
np.random.shuffle(arr2)
np.random.shuffle(arr3)
# print(arr0)
# print(arr1)
# print(arr2)
# print(arr3)
data_origin = data_origin[arr0]
data_flip_a = data_flip_a[arr1]
data_flip_b = data_flip_b[arr2]
data_flip_c = data_flip_c[arr3]

# 开始数据增广
data_all = []      # 用于汇总增广后新增的数据
for i in range(abnormal_count):
    data_tmp = data_origin[i]
    data_tmp_a = data_flip_a[i]
    data_tmp_b = data_flip_b[i]
    data_tmp_c = data_flip_c[i]

    data_tmp_0 = (data_tmp + data_tmp_a) / 2.0
    data_tmp_1 = (data_tmp + data_tmp_b) / 2.0
    data_tmp_2 = (data_tmp + data_tmp_c) / 2.0
    data_tmp_3 = (data_tmp_a + data_tmp_b) / 2.0
    data_tmp_4 = (data_tmp_a + data_tmp_c) / 2.0
    data_tmp_5 = (data_tmp_b + data_tmp_c) / 2.0
    data_tmp_0 = data_tmp_0.reshape(1, 60)
    data_tmp_1 = data_tmp_1.reshape(1, 60)
    data_tmp_2 = data_tmp_2.reshape(1, 60)
    data_tmp_3 = data_tmp_3.reshape(1, 60)
    data_tmp_4 = data_tmp_4.reshape(1, 60)
    data_tmp_5 = data_tmp_5.reshape(1, 60)

    if i == 0:
        data_all = np.row_stack((data_tmp_0, data_tmp_1, data_tmp_2, data_tmp_3, data_tmp_4, data_tmp_5))
    else:
        data_all = np.row_stack((data_all, data_tmp_0, data_tmp_1, data_tmp_2, data_tmp_3, data_tmp_4, data_tmp_5))
# print(data_all.shape)
data_new = np.row_stack((data, data_all))
data_flip_a = data_flip_a.reshape(abnormal_count,60)
data_flip_b = data_flip_b.reshape(abnormal_count,60)
data_flip_c = data_flip_c.reshape(abnormal_count,60)
data_new = np.row_stack((data_new, data_flip_a, data_flip_b, data_flip_c))
labels_new = labels
labels_new = labels_new.reshape(labels.shape[0],1)
for i in range(abnormal_count*9):
    labels_new = np.row_stack((labels_new,np.array([[1]])))
# print(data_new.shape)
# print(labels_new.shape)
# checking
# abnormal_count_new = 0
# for i in range(labels_new.shape[0]):
#     if labels_new[i] == 1:
#         abnormal_count_new = abnormal_count_new + 1
# print(abnormal_count_new)
np.savetxt("training_fr_timeChroma_new/training data.txt", data_new)
np.savetxt("training_fr_timeChroma_new/labels.txt", labels_new)