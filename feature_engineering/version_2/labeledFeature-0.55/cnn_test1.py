# -*- coding: utf-8 -*-
from skimage import io,transform
import tensorflow as tf
from travel_path import *

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

signal_dict = {0:'正常无风舞信号',1:'异常有风舞信号'}

w=40
h=96
c=3

# 测试集地址
path = 'test_set/'
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
        img = transform.resize(b,(40,96,3))
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
label = labels.reshape(labels.shape[0]*labels.shape[1],)
print(data.shape)
print(label.shape)

with tf.Session() as sess:
    saver = tf.train.import_meta_graph('model/model.ckpt-0.meta')
    saver.restore(sess, tf.train.latest_checkpoint('model/'))

    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name("x:0")
    feed_dict = {x:data}

    logits = graph.get_tensor_by_name("logits_eval:0")

    classification_result = sess.run(logits,feed_dict)

    #打印出预测矩阵
    print(classification_result)
    #打印出预测矩阵每一行最大值的索引
    print(tf.argmax(classification_result,1).eval())
    #根据索引通过字典对应花的分类
    output = []
    output = tf.argmax(classification_result,1).eval()
    count = 0
    count_abnormal = 0
    total_abnormal = 0
    for i in range(len(output)):
        print("第",i+1,"帧信号识别:"+signal_dict[output[i]])
        if label[i] == 1:
            total_abnormal = total_abnormal + 1
        if output[i] == label[i]:
            count = count + 1
            if label[i] == 1:
                count_abnormal = count_abnormal + 1
    print("信号识别准确率：",count/label.shape[0])
    print("异常信号识别准确率：",count_abnormal/total_abnormal)
    # 记录下每一步的损失函数和训练之后的准确率
    if os.path.exists('test_acc/test acc in every step training model.txt'):
        data_tmp = np.genfromtxt('test_acc/test acc in every step training model.txt')
        data_tmp = data_tmp.reshape(data_tmp.shape[0], 1)
        data_i = np.array([count/label.shape[0]])
        data = np.row_stack((data_tmp, data_i))
        np.savetxt('test_acc/test acc in every step training model.txt', data)
    else:
        data = np.array([count/label.shape[0]])
        print(data.shape)
        np.savetxt('test_acc/test acc in every step training model.txt', data)
    if os.path.exists('test_acc/test abnormal acc in every step training model.txt'):
        data_tmp = np.genfromtxt('test_acc/test abnormal acc in every step training model.txt')
        data_tmp = data_tmp.reshape(data_tmp.shape[0], 1)
        data_i = np.array([count_abnormal/total_abnormal])
        data = np.row_stack((data_tmp, data_i))
        np.savetxt('test_acc/test abnormal acc in every step training model.txt', data)
    else:
        data = np.array([count_abnormal/total_abnormal])
        print(data.shape)
        np.savetxt('test_acc/test abnormal acc in every step training model.txt', data)
