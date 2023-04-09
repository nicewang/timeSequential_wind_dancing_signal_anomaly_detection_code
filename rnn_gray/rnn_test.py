import tensorflow as tf
from helpers import AttrDict
from SequenceLabellingModel import SequenceLabellingModel
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
    data,label = getDataLabel(path)
    data = data.reshape(data.shape[:2] + (-1,))
    order = np.random.permutation(len(data))
    data = data[order]
    label = label[order]
    return data, label

test_data, test_target = get_dataset('test_set_new/')
print(test_data.shape)
print(test_target.shape)

abnormal_count = 0
for i in range(test_target.shape[0]):
    for j in range(test_target.shape[1]):
        if test_target[i,j,0] == 1:
            abnormal_count = abnormal_count + 1
print('abnormal_count in test:',abnormal_count)

with tf.Session() as sess:
    saver = tf.train.import_meta_graph('model/model.ckpt.meta')
    saver.restore(sess, tf.train.latest_checkpoint('model/'))

    _, length1, image_size1 = test_data.shape
    num_classes1 = test_target.shape[2]
    data1 = tf.placeholder(tf.float32, [None, length1, image_size1])
    target1 = tf.placeholder(tf.float32, [None, length1, num_classes1])
    model1 = SequenceLabellingModel(data1, target1, params)

    test_feed = {data1: test_data, target1: test_target}
    test_error, _ = sess.run([model1.error, model1.optimize], test_feed)
    print('Test error: {:3.6f}%'.format(100 * test_error))
