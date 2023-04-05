# -*- coding: utf-8 -*-
import tensorflow as tf
from travel_path import *
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

signal_dict = {0:'正常无风舞信号',1:'异常有风舞信号'}

w = 5
h = 12
c = 1

data = []
data_tmp = np.genfromtxt("train_abnormal_set/data.txt")
for j in range(data_tmp.shape[0]):
    data_tmp2 = data_tmp[j,:]
    data_tmp2 = data_tmp2.reshape(5, 12)
    b = np.zeros((5, 12, 1))
    for i1 in range(5):
        for j1 in range(12):
            b[i1, j1, 0] = data_tmp2[i1, j1]
    img = b
    data.append(img)

data = np.asarray(data,np.float32)
# print(data.shape)
# print(label.shape)

with tf.Session() as sess:
    saver = tf.train.import_meta_graph('model/model.ckpt-' + sys.argv[1] + '.meta')
    saver.restore(sess,tf.train.latest_checkpoint('model/'))

    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name("x:0")
    feed_dict = {x:data}

    logits = graph.get_tensor_by_name("logits_eval:0")

    classification_result = sess.run(logits,feed_dict)

    #打印出预测矩阵
    # print(classification_result)
    #打印出预测矩阵每一行最大值的索引
    # print(tf.argmax(classification_result,1).eval())
    #根据索引通过字典对应花的分类
    output = []
    output = tf.argmax(classification_result,1).eval()

    count_abnormal = 0
    for i in range(len(output)):
        # print("第",i+1,"帧信号识别:"+signal_dict[output[i]])
        if output[i] == 1:
            count_abnormal = count_abnormal + 1
    print(count_abnormal)
    if os.path.exists('test_acc/count_abnormal_train.txt'):
        data_tmp = np.genfromtxt('test_acc/count_abnormal_train.txt')
        data_tmp = np.array([data_tmp])
        if data_tmp.shape != (1,):
            data_tmp = data_tmp.reshape(data_tmp.shape[0]*data_tmp.shape[1],1)
        data_i = np.array([[count_abnormal]])
        data = np.row_stack((data_tmp, data_i))
        np.savetxt('test_acc/count_abnormal_train.txt', data)
    else:
        data = np.array([count_abnormal])
        np.savetxt('test_acc/count_abnormal_train.txt', data)
