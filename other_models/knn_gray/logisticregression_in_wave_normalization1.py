from sklearn.linear_model import LogisticRegression
from travel_path import *
import numpy as np

clf = LogisticRegression()

def lr_model(clf, X):
    # print(np.mean(1 / (1 + np.exp(-(clf.intercept_ + clf.coef_ * X)))))
    if np.mean(1 / (1 + np.exp(-(clf.intercept_ + clf.coef_*X)))) > 0.9999:
        return 1
    else:
        return 0

# train_data_files = travel_txt("original_onePointData_normalization1/train_set")
# train_label_files = travel_txt("labels-0.55/train_set")
# train
# data_new = []
# labels_new = []
# for i in range(train_data_files.shape[0]):
#     data = np.genfromtxt(train_data_files[i])
#     labels = np.genfromtxt(train_label_files[i])
#     # print(data.shape)
#     # print(labels.shape)
#     if data_new == []:
#         data_new = data
#         labels_new = labels
#         labels_new = labels_new.reshape(labels_new.shape[0],1)
#     else:
#         for j in range(data.shape[0]):
#             data_tmp = data[j, :]
#             data_tmp = data_tmp.reshape(1,100)
#             data_new = np.row_stack((data_new, data_tmp))
#             labels_tmp = np.array([labels[j]])
#             labels_tmp = labels_tmp.reshape(1,1)
#             labels_new = np.row_stack((labels_new, labels_tmp))
#     print(data_new.shape)
#     print(labels_new.shape)
#     # knn.fit(data, labels)
#     # for j in range(data.shape[0]):
#     #     data_tmp = data[j,:]
#     #     data_tmp = data_tmp.reshape(1,100)
#     #     label = np.array([labels[j]])
#     #     # print(data_tmp.shape)
#     #     # print(label.shape)
#     #     knn.fit(data_tmp, label)
# labels_new = labels_new.reshape(labels_new.shape[0],)

data_new = np.genfromtxt("training_fr_wave_normalization1/training data.txt")
labels_new = np.genfromtxt("training_fr_wave_normalization1/labels.txt")
clf.fit(data_new, labels_new)

# np.savetxt("training_fr_wave_normalization1/training data.txt", data_new)
# np.savetxt("training_fr_wave_normalization1/labels.txt", labels_new)
# test
test_data_files = travel_txt("original_onePointData_normalization1/test_set")
test_label_files = travel_txt("labels-0.55/test_set")
signal_dict = {0:'正常无风舞信号',1:'异常有风舞信号'}
count_abnormal = 0
total_abnormal = 0
count = 0
total = 0
for i in range(test_data_files.shape[0]):
    data = np.genfromtxt(test_data_files[i])
    labels = np.genfromtxt(test_label_files[i])
    if total == 0:
        total = labels.shape[0]
    else:
        total = total + labels.shape[0]
    for j in range(data.shape[0]):
        data_tmp = data[j,:]
        data_tmp = data_tmp.reshape(1,100)
        # result = lr_model(clf, data_tmp)
        result = clf.predict(data_tmp)
        result = np.asarray(result)
        result1 = result[0]
        print("第", i + 1, "个测试集文件","第", j + 1, "帧信号识别:" + signal_dict[result1])
        if labels[j] == 1:
            total_abnormal = total_abnormal + 1
            if result == 1:
                count_abnormal = count_abnormal + 1
        if labels[j] == result:
            count = count + 1
        # print("第", i + 1, "个测试集文件", "第", j + 1, "帧信号识别:")
        # print(result1)
        # print(result.shape)
print(count_abnormal)
print(total_abnormal)
print("异常信号识别准确率：", count_abnormal/total_abnormal)
print(count)
print(total)
print("所有信号识别准确率：", count/total)
