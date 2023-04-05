# -*- coding: utf-8 -*-
from travel_path import *
import numpy as np
import tensorflow as tf
import time
from subprocess import call

import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

w = 5
h = 12
c = 1

model_path = "model/model.ckpt"

data0 = np.genfromtxt("training_fr_timeChroma_new_1/training data.txt")
label = np.genfromtxt("training_fr_timeChroma_new_1/labels.txt")
data = []
for i in range(data0.shape[0]):
    data_tmp = data0[i,:]
    data_tmp = data_tmp.reshape(5,12)
    b = np.zeros((5, 12, 1))
    for i1 in range(5):
        for j1 in range(12):
            b[i1, j1, 0] = data_tmp[i1, j1]
    img = b
    data.append(img)
data = np.asarray(data,np.float32)
print(data.shape)
print(label.shape)

# 打乱顺序
num_example = data.shape[0]
arr = np.arange(num_example)
np.random.shuffle(arr)
data = data[arr]
label = label[arr]

x_train = data
y_train = label

#-----------------构建网络----------------------
#占位符
x = tf.placeholder(tf.float32,shape = [None,w,h,c],name='x')
y_ = tf.placeholder(tf.int32,shape = [None,],name='y_')

def inference(input_tensor, train, regularizer):
    with tf.variable_scope('layer1-conv1'):
        conv1_weights = tf.get_variable("weight", [5, 5, 1, 128],
                                        initializer=tf.truncated_normal_initializer(stddev=0.1))
        # 可视化观看变量
        tf.summary.histogram("layer1-conv1/weights",conv1_weights)
        conv1_biases = tf.get_variable("bias", [128], initializer=tf.constant_initializer(0.0))
        # 可视化观看变量
        tf.summary.histogram("layer1-conv1/biases", conv1_biases)
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))

    with tf.name_scope("layer2-pool1"):
        pool1 = tf.nn.max_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="VALID")

    with tf.variable_scope("layer3-conv2"):
        conv2_weights = tf.get_variable("weight", [5, 5, 128, 256],
                                        initializer=tf.truncated_normal_initializer(stddev=0.1))
        # 可视化观看变量
        tf.summary.histogram("layer3-conv2/weights", conv2_weights)
        conv2_biases = tf.get_variable("bias", [256], initializer=tf.constant_initializer(0.0))
        # 可视化观看变量
        tf.summary.histogram("layer3-conv2/biases", conv2_biases)
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1, 1, 1, 1], padding='SAME')
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))

    with tf.name_scope("layer4-pool2"):
        pool2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
        nodes = 1 * 3 * 256
        reshaped = tf.reshape(pool2, [-1, nodes])

    with tf.variable_scope('layer5-fc1'):
        fc2_weights = tf.get_variable("weight", [nodes, 512],
                                      initializer=tf.truncated_normal_initializer(stddev=0.1))
        tf.summary.histogram("layer5-fc1/weights", fc2_weights)
        if regularizer != None: tf.add_to_collection('losses', regularizer(fc2_weights))
        fc2_biases = tf.get_variable("bias", [512], initializer=tf.constant_initializer(0.1))
        tf.summary.histogram("layer5-fc1/biases", fc2_biases)

        fc2 = tf.nn.relu(tf.matmul(reshaped, fc2_weights) + fc2_biases)
        if train: fc2 = tf.nn.dropout(fc2, 0.5)

    with tf.variable_scope('layer6-fc2'):
        fc3_weights = tf.get_variable("weight", [512, 2],
                                      initializer=tf.truncated_normal_initializer(stddev=0.1))
        tf.summary.histogram("layer6-fc2/weights", fc3_weights)
        if regularizer != None: tf.add_to_collection('losses', regularizer(fc3_weights))
        fc3_biases = tf.get_variable("bias", [2], initializer=tf.constant_initializer(0.1))
        tf.summary.histogram("layer6-fc2/biases", fc3_biases)
        logit = tf.matmul(fc2, fc3_weights) + fc3_biases

    return logit

#---------------------------网络结束---------------------------
regularizer = tf.contrib.layers.l2_regularizer(0.0001)
logits = inference(x,False,regularizer)

#(小处理)将logits乘以1赋值给logits_eval，定义name，方便在后续调用模型时通过tensor名字调用输出tensor
b = tf.constant(value=1,dtype=tf.float32)
logits_eval = tf.multiply(logits,b,name='logits_eval')

loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y_)
train_op = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)
correct_prediction = tf.equal(tf.cast(tf.argmax(logits,1),tf.int32), y_)
acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


#定义一个函数，按批次取数据
def minibatches(inputs=None, targets=None, batch_size=None, shuffle=False):
    assert len(inputs) == len(targets)
    if shuffle:
        indices = np.arange(len(inputs))
        np.random.shuffle(indices)
    for start_idx in range(0, len(inputs) - batch_size + 1, batch_size):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batch_size]
        else:
            excerpt = slice(start_idx, start_idx + batch_size)
        yield inputs[excerpt], targets[excerpt]

#训练和测试数据，可将n_epoch设置更大一些
n_epoch = 30
batch_size = 64
saver = tf.train.Saver()
sess = tf.Session()
# 合并到Summary中
merged = tf.summary.merge_all()
# 选定可视化存储目录
writer = tf.summary.FileWriter("graph/", sess.graph)
sess.run(tf.global_variables_initializer())

initial_step = 0

# 验证之前是否已经保存了检查点文件
ckpt = tf.train.get_checkpoint_state('model/')
if ckpt and ckpt.model_checkpoint_path:
    saver.restore(sess, ckpt.model_checkpoint_path)
    initial_step = int(ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1])
    print(initial_step)
    initial_step = initial_step + 1

for epoch in range(initial_step, n_epoch):
    start_time = time.time()

    print("initial_step: ", initial_step)

    #training
    train_loss, train_acc, n_batch = 0, 0, 0
    for x_train_a, y_train_a in minibatches(x_train, y_train, batch_size, shuffle=True):
        _,err,ac = sess.run([train_op,loss,acc], feed_dict={x: x_train_a, y_: y_train_a})
        train_loss += err; train_acc += ac; n_batch += 1
    print("train loss: %f" % (np.sum(train_loss)/n_batch))
    print("train acc: %f" % (np.sum(train_acc)/n_batch))
    tf.summary.scalar('train loss', np.sum(train_loss)/n_batch)
    tf.summary.scalar('train accuracy', np.sum(train_acc)/n_batch)

    # 记录下每一步的损失函数和训练之后的准确率
    if os.path.exists('loss_acc/loss in every step training model.txt'):
        data_tmp = np.genfromtxt('loss_acc/loss in every step training model.txt')
        if epoch > 1:
            print(data_tmp.shape)
            data_tmp = data_tmp.reshape(data_tmp.shape[0],1)
        data_i = np.array([(np.sum(train_loss)/n_batch)])
        data = np.row_stack((data_tmp, data_i))
        np.savetxt('loss_acc/loss in every step training model.txt', data)
    else:
        data = np.array([(np.sum(train_loss)/n_batch)])
        print(data.shape)
        np.savetxt('loss_acc/loss in every step training model.txt', data)
    if os.path.exists('loss_acc/acc in every step training model.txt'):
        data_tmp = np.genfromtxt('loss_acc/acc in every step training model.txt')
        if epoch > 1:
            print(data_tmp.shape)
            data_tmp = data_tmp.reshape(data_tmp.shape[0],1)
        data_i = np.array([(np.sum(train_acc)/n_batch)])
        data = np.row_stack((data_tmp, data_i))
        np.savetxt('loss_acc/acc in every step training model.txt', data)
    else:
        data = np.array([(np.sum(train_acc)/n_batch)])
        print(data.shape)
        np.savetxt('loss_acc/acc in every step training model.txt', data)

    if (epoch+1)%5 == 0:
        result = sess.run(merged,feed_dict={x: x_train_a, y_: y_train_a})
        writer.add_summary(result, epoch+1)

    saver.save(sess, model_path, global_step=epoch)
    call("python cnn_test1.py " + str(epoch), shell=True)
    call("python cnn_test2.py " + str(epoch), shell=True)

saver.save(sess, model_path, global_step=n_epoch-1)
sess.close()
