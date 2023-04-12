# -*- coding: utf-8 -*-
from travel_path import *
from skimage import transform
import tensorflow as tf
import time
from subprocess import call

import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

w = 5
h = 50
c = 1

# path = 'train_set/'
# files = travel_txt(path)

model_path = "model/model.ckpt"

# data = []
# labels = []
# for i in range(files.shape[0]):
#     data_tmp = np.genfromtxt(files[i])
#     data_tmp1 = data_tmp[:60,:]
#     for j in range(data_tmp1.shape[1]):
#         data_tmp2 = data_tmp1[:,j]
#         data_tmp2 = data_tmp2.reshape(5, 12)
#
#         # b = []
#         # for ia in range(8 - 1):
#         #     for ja in range(data_tmp2.shape[0]):
#         #         if b == []:
#         #             b = data_tmp2
#         #             b = np.row_stack((b, data_tmp2[ja, :]))
#         #         else:
#         #             b = np.row_stack((b, data_tmp2[ja, :]))
#         # c = []
#         # for ia in range(8 - 1):
#         #     for ja in range(data_tmp2.shape[1]):
#         #         if c == []:
#         #             c = b
#         #             c = np.column_stack((c, b[:, ja]))
#         #         else:
#         #             c = np.column_stack((c, b[:, ja]))
#
#         b = np.zeros((5, 12, 1))
#         for i1 in range(5):
#             for j1 in range(12):
#                 b[i1, j1, 0] = data_tmp2[i1, j1]
#                 # b[i1, j1, 1] = data_tmp2[i1, j1]
#                 # b[i1, j1, 2] = data_tmp2[i1, j1]
#         img = transform.resize(b,(10,24,1))
#
#         # d = np.zeros((40, 96, 3))
#         # for i1 in range(40):
#         #     for j1 in range(96):
#         #         d[i1, j1, 0] = c[i1, j1]
#         #         d[i1, j1, 1] = c[i1, j1]
#         #         d[i1, j1, 2] = c[i1, j1]
#         # img = transform.resize(d, (40, 96, 3))
#         data.append(img)
#     label_tmp1 = data_tmp[60,:]
#     label_tmp1 = label_tmp1.reshape(1,label_tmp1.shape[0])
#     # if data == []:
#     #     data = data_tmp1
#     # else:
#     #     data = np.column_stack((data, data_tmp1))
#     if labels == []:
#         labels = label_tmp1
#     else:
#         labels = np.column_stack((labels, label_tmp1))

data0 = np.genfromtxt("training_fr_timeFreq/training data.txt")
label = np.genfromtxt("training_fr_timeFreq/labels.txt")
data = []
for i in range(data0.shape[0]):
    data_tmp = data0[i,:]
    data_tmp = data_tmp.reshape(5,50)
    b = np.zeros((5, 50, 1))
    for i1 in range(5):
        for j1 in range(50):
            b[i1, j1, 0] = data_tmp[i1, j1]
            # b[i1, j1, 1] = data_tmp2[i1, j1]
            # b[i1, j1, 2] = data_tmp2[i1, j1]
    # img = transform.resize(b,(10,24,1))
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

"""
# 将所有数据分为训练集和验证集
ratio = 7.0/9.0
print ratio
s = np.int(num_example*ratio)
x_train = data[:s]
y_train = label[:s]
x_val = data[s:]
y_val = label[s:]
print x_train.shape
print x_val.shape """

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
        nodes = 1 * 12 * 256
        reshaped = tf.reshape(pool2, [-1, nodes])

    # with tf.variable_scope("layer5-conv3"):
    #     conv3_weights = tf.get_variable("weight", [3, 3, 128, 256],
    #                                     initializer=tf.truncated_normal_initializer(stddev=0.1))
    #     # 可视化观看变量
    #     tf.summary.histogram("layer5-conv3/weights", conv3_weights)
    #     conv3_biases = tf.get_variable("bias", [256], initializer=tf.constant_initializer(0.0))
    #     # 可视化观看变量
    #     tf.summary.histogram("layer5-conv3/biases", conv3_biases)
    #     conv3 = tf.nn.conv2d(pool2, conv3_weights, strides=[1, 1, 1, 1], padding='SAME')
    #     relu3 = tf.nn.relu(tf.nn.bias_add(conv3, conv3_biases))
    #
    # with tf.name_scope("layer6-pool3"):
    #     pool3 = tf.nn.max_pool(relu3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
    #     nodes = 1 * 3 * 256
    #     reshaped = tf.reshape(pool3, [-1, nodes])
    #
    # with tf.variable_scope("layer7-conv4"):
    #     conv4_weights = tf.get_variable("weight", [3, 3, 128, 128],
    #                                     initializer=tf.truncated_normal_initializer(stddev=0.1))
    #     # 可视化观看变量
    #     tf.summary.histogram("layer7-conv4/weights", conv4_weights)
    #     conv4_biases = tf.get_variable("bias", [128], initializer=tf.constant_initializer(0.0))
    #     # 可视化观看变量
    #     tf.summary.histogram("layer7-conv4/biases", conv4_biases)
    #     conv4 = tf.nn.conv2d(pool3, conv4_weights, strides=[1, 1, 1, 1], padding='SAME')
    #     relu4 = tf.nn.relu(tf.nn.bias_add(conv4, conv4_biases))
    #
    # with tf.name_scope("layer8-pool4"):
    #     pool4 = tf.nn.max_pool(relu4, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
    #     # nodes = 6 * 6 * 128
    #     nodes = 2 * 6 * 128
    #     reshaped = tf.reshape(pool4, [-1, nodes])

    # with tf.variable_scope('layer9-fc1'):
    #     fc1_weights = tf.get_variable("weight", [nodes, 1024],
    #                                   initializer=tf.truncated_normal_initializer(stddev=0.1))
    #     tf.summary.histogram("layer9-fc1/weights", fc1_weights)
    #     if regularizer != None: tf.add_to_collection('losses', regularizer(fc1_weights))
    #     fc1_biases = tf.get_variable("bias", [1024], initializer=tf.constant_initializer(0.1))
    #     # 可视化观看变量
    #     tf.summary.histogram("layer9-fc1/biases", fc1_biases)
    #
    #     fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)
    #     if train: fc1 = tf.nn.dropout(fc1, 0.5)
    #
    # with tf.variable_scope('layer10-fc2'):
    #     fc2_weights = tf.get_variable("weight", [1024, 512],
    #                                   initializer=tf.truncated_normal_initializer(stddev=0.1))
    #     tf.summary.histogram("layer10-fc2/weights", fc2_weights)
    #     if regularizer != None: tf.add_to_collection('losses', regularizer(fc2_weights))
    #     fc2_biases = tf.get_variable("bias", [512], initializer=tf.constant_initializer(0.1))
    #     tf.summary.histogram("layer10-fc2/biases", fc2_biases)
    #
    #     fc2 = tf.nn.relu(tf.matmul(fc1, fc2_weights) + fc2_biases)
    #     if train: fc2 = tf.nn.dropout(fc2, 0.5)
    #
    # with tf.variable_scope('layer11-fc3'):
    #     fc3_weights = tf.get_variable("weight", [512, 4],
    #                                   initializer=tf.truncated_normal_initializer(stddev=0.1))
    #     tf.summary.histogram("layer11-fc3/weights", fc3_weights)
    #     if regularizer != None: tf.add_to_collection('losses', regularizer(fc3_weights))
    #     fc3_biases = tf.get_variable("bias", [4], initializer=tf.constant_initializer(0.1))
    #     tf.summary.histogram("layer11-fc3/biases", fc3_biases)
    #     logit = tf.matmul(fc2, fc3_weights) + fc3_biases

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
        fc3_weights = tf.get_variable("weight", [512, 4],
                                      initializer=tf.truncated_normal_initializer(stddev=0.1))
        tf.summary.histogram("layer6-fc2/weights", fc3_weights)
        if regularizer != None: tf.add_to_collection('losses', regularizer(fc3_weights))
        fc3_biases = tf.get_variable("bias", [4], initializer=tf.constant_initializer(0.1))
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

n_epoch = 500
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

"""    #validation
    if n_epoch % 10 == 0:
        val_loss, val_acc, n_batch = 0, 0, 0
        for x_val_a, y_val_a in minibatches(x_val, y_val, batch_size, shuffle=False):
            err, ac = sess.run([loss,acc], feed_dict={x: x_val_a, y_: y_val_a})
            val_loss += err; val_acc += ac; n_batch += 1
        print "validation loss: %f" % (np.sum(val_loss)/ n_batch)
        print "validation acc: %f" % (np.sum(val_acc)/ n_batch) """
saver.save(sess, model_path, global_step=n_epoch-1)
sess.close()
