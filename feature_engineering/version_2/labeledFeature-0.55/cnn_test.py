# -*- coding: utf-8 -*-
from skimage import io,transform
import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

flower_dict = {0:'水中战斗舰艇',1:'水面战斗舰艇',2:'特种战斗舰艇',3:'辅助舰艇'}

w=100
h=100
c=3

# 测试集地址
path = "test_set/Labeled Feature of Point at 7.1km.txt"

def read_one_image(path):
    img = io.imread(path)
    img = transform.resize(img,(w,h))
    return np.asarray(img)

with tf.Session() as sess:
    data_tmp = np.genfromtxt(path)
    data_tmp1 = data_tmp[:60, :]
    data = []
    for j in range(data_tmp1.shape[1]):
        data_tmp2 = data_tmp1[:, j]
        data_tmp2 = data_tmp2.reshape(5, 12)
        b = np.zeros((5, 12, 3))
        for i1 in range(5):
            for j1 in range(12):
                b[i1, j1, 0] = data_tmp2[i1, j1]
                b[i1, j1, 1] = data_tmp2[i1, j1]
                b[i1, j1, 2] = data_tmp2[i1, j1]
        img = transform.resize(b, (100, 100, 3))
        data.append(img)
    label_tmp1 = data_tmp[60, :]

    data = np.asarray(data, np.float32)
    label = label_tmp1

    print(data.shape)
    print(label.shape)

    saver = tf.train.import_meta_graph('model/model.ckpt-56.meta')
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
        print("第",i+1,"帧信号识别:"+flower_dict[output[i]])
        if label[i] == 1:
            total_abnormal = total_abnormal + 1
        if output[i] == label[i]:
            count = count + 1
            if label[i] == 1:
                count_abnormal = count_abnormal + 1
    print("信号识别准确率：",count/label.shape[0])
    print("异常信号识别准确率：",count_abnormal/total_abnormal)
