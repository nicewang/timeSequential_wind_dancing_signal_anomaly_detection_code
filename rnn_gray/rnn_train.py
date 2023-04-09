import tensorflow as tf
from helpers import AttrDict
from SequenceLabellingModel import SequenceLabellingModel
from batched import batched
from SignalDataSet import *

import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

params = AttrDict(
    rnn_cell=tf.nn.rnn_cell.GRUCell,
    rnn_hidden=300,
    optimizer=tf.train.RMSPropOptimizer(0.002),
    gradient_clipping=5,
    batch_size=10,
    epochs=5,
    epoch_size=50
)

def get_dataset(path):
    # Flatten images into vectors.
    # path = 'train_set/'
    data,label = getDataLabel(path)
    data = data.reshape(data.shape[:2] + (-1,))
    # One-hot encode labels.
    label0 = np.copy(label)
    label0 = label0.reshape(label0.shape[0],label0.shape[1])
    label1 = np.zeros(label0.shape + (2,))
    for i in range(label.shape[0]):
        for j in range(label.shape[1]):
            if label[i,j,0] == 1:
                label1[i,j,0] = 1
            else:
                label1[i,j,1] = 1
    # Shuffle order of examples.
    label = label1
    order = np.random.permutation(len(data))
    data = data[order]
    label = label[order]
    return data, label


# Split into training and test data.
train_data, train_target = get_dataset('train_set/')
print(train_data.shape)
print(train_target.shape)
test_data, test_target = get_dataset('test_set/')
print(test_data.shape)
print(test_target.shape)
abnormal_data = []
abnormal_target = []
for i in range(test_target.shape[0]):
    for j in range(test_target.shape[1]):
        if test_target[i,j,0] == 1:
            abnormal_data.append(test_data[i, j])
            abnormal_target.append(test_target[i, j])
abnormal_data = np.array(abnormal_data)
abnormal_target = np.array(abnormal_target)
abnormal_data = abnormal_data.reshape(16,12,60)
abnormal_target = abnormal_target.reshape(16,12,2)
# split = int(0.66 * len(data))
# train_data, test_data = data[:split], data[split:]
# train_target, test_target = target[:split], target[split:]

# Compute graph.
_, length, image_size = train_data.shape
num_classes = train_target.shape[2]
print(length, image_size, num_classes)
data = tf.placeholder(tf.float32, [None, length, image_size])
target = tf.placeholder(tf.float32, [None, length, num_classes])
model = SequenceLabellingModel(data, target, params)
batches = batched(train_data, train_target, params.batch_size)

abnormal_count = 0
for i0 in range(train_target.shape[0]):
    for j0 in range(train_target.shape[1]):
        if train_target[i0,j0,0] == 1:
            abnormal_count = abnormal_count + 1
print('abnormal_count in train:',abnormal_count)

saver = tf.train.Saver()

sess = tf.Session()
sess.run(tf.initialize_all_variables())
for index, batch in enumerate(batches):
    batch_data = batch[0]
    batch_target = batch[1]
    epoch = batch[2]
    if epoch >= params.epochs:
        break
    feed = {data: batch_data, target: batch_target}
    error, _ = sess.run([model.error, model.optimize], feed)
    print('{}: {:3.6f}%'.format(index + 1, 100 * error))
    test_feed = {data: test_data, target: test_target}
    test_error, _ = sess.run([model.error, model.cost], test_feed)
    print('Test error: {:3.6f}%'.format(100 * test_error))
    abnormal_feed = {data: abnormal_data, target: abnormal_target}
    abnormal_error, _ = sess.run([model.error, model.cost], abnormal_feed)
    print('Abnormal error: {:3.6f}%'.format(100 * abnormal_error))

# model_path = 'model/model.ckpt'
# saver.save(sess, model_path)
# sess.close()

abnormal_count = 0
for i1 in range(test_target.shape[0]):
    for j1 in range(test_target.shape[1]):
        if test_target[i1,j1,0] == 1:
            abnormal_count = abnormal_count + 1
print('abnormal_count in test target:',abnormal_count)

test_feed = {data: test_data, target: test_target}
test_error, _ = sess.run([model.error, model.cost], test_feed)
print('Test error: {:3.6f}%'.format(100 * test_error))
abnormal_feed = {data: abnormal_data, target: abnormal_target}
abnormal_error, _ = sess.run([model.error, model.cost], abnormal_feed)
print('Abnormal error: {:3.6f}%'.format(100 * abnormal_error))
# prediction = sess.run([model.prediction], {data: test_data})
# prediction = np.array(prediction)
# print(prediction.shape)

