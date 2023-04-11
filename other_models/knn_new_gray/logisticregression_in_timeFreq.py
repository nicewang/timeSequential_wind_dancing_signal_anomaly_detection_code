from sklearn.linear_model import LogisticRegression
from travel_path import *
import numpy as np

def logistic_train(C):
    clf = LogisticRegression(C=C)

    def lr_model(clf, X):
        # print(np.mean(1 / (1 + np.exp(-(clf.intercept_ + clf.coef_ * X)))))
        if np.mean(1 / (1 + np.exp(-(clf.intercept_ + clf.coef_*X)))) > 0.0012:
            return 1
        else:
            return 0

    # path = 'labeledFeature-0.55/train_set/'
    # files = travel_txt(path)

    # train
    # data = []
    # labels = []
    # for i in range(files.shape[0]):
    #     data_tmp = np.genfromtxt(files[i])
    #     # print(data_tmp.shape)
    #     data_tmp1 = data_tmp[:60,:]
    #     data_tmp1 = np.transpose(data_tmp1)
    #     label_tmp1 = data_tmp[60,:]
    #     if data == []:
    #         data = data_tmp1
    #         labels = label_tmp1
    #         labels = labels.reshape(labels.shape[0],1)
    #     else:
    #         for j in range(data_tmp1.shape[0]):
    #             data_tmp2 = data_tmp1[j,:]
    #             data_tmp2 = data_tmp2.reshape(1, 60)
    #             data = np.row_stack((data, data_tmp2))
    #             label_tmp2 = np.array([label_tmp1[j]])
    #             label_tmp2 = label_tmp2.reshape(1,1)
    #             labels = np.row_stack((labels, label_tmp2))
    #     print(data.shape)
    #     print(labels.shape)
    # labels = labels.reshape(labels.shape[0],)

    data = np.genfromtxt("training_fr_timeFreq/training data.txt")
    labels = np.genfromtxt("training_fr_timeFreq/labels.txt")
    clf.fit(data, labels)

    # np.savetxt("training_fr_timeChroma/training data.txt", data)
    # np.savetxt("training_fr_timeChroma/labels.txt", labels)

    # test
    path = 'test_set/'
    files = travel_txt(path)
    signal_dict = {0:'正常无风舞信号',1:'异常有风舞信号'}
    count_abnormal = 0
    total_abnormal = 0
    count = 0
    total = 0
    for i in range(files.shape[0]):
        data_tmp = np.genfromtxt(files[i])
        data_tmp1 = data_tmp[:250,:]
        data_tmp1 = np.transpose(data_tmp1)
        label_tmp1 = data_tmp[250,:]
        if total == 0:
            total = label_tmp1.shape[0]
        else:
            total = total + label_tmp1.shape[0]
        for j in range(data_tmp1.shape[0]):
            data_tmp2 = data_tmp1[j,:]
            data_tmp2 = data_tmp2.reshape(1,250)
            # result = lr_model(clf, data_tmp2)
            result = clf.predict(data_tmp2)
            result = np.asarray(result)
            result1 = result[0]
            # print("第", i + 1, "个测试集文件","第", j + 1, "帧信号识别:" + signal_dict[result1])
            if label_tmp1[j] == 1:
                total_abnormal = total_abnormal + 1
                if result == 1:
                    count_abnormal = count_abnormal + 1
            if label_tmp1[j] == result:
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
    return count_abnormal, count

count = []
count_abnormal = []
C = [1e0, 1e5, 1e10, 1e15, 1e20]
for i in range(5):
    count_abnormal_tmp, count_tmp = logistic_train(C[i])
    if i == 0:
        count = count_tmp
        count_abnormal = count_abnormal_tmp
    else:
        count = np.row_stack((count, count_tmp))
        count_abnormal = np.row_stack((count_abnormal, count_abnormal_tmp))
data_new = np.column_stack((count_abnormal,count))
print(data_new.shape)
np.savetxt("logistic_result/logistic_result0/liblinear/result.txt", data_new)