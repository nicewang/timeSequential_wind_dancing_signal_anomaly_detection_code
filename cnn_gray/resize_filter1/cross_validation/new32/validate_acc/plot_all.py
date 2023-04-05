import numpy as np
import pylab as pl

pl.figure(figsize=(7,9))

pl.subplot(411)
data = np.genfromtxt('count.txt')
data = data/5184.0
pl.plot(data,linewidth=0.7,color='blue',label='Validating Accuracy')
data1 = np.genfromtxt('acc in every step training model.txt')
pl.plot(data1,linewidth=0.7,label='Training Accuracy')
pl.axvline(23,color='k',linewidth=0.5,linestyle="--")
pl.title("Accuracy Rate Varies with Training Epochs")
pl.xlabel('Epoch')
pl.legend()

pl.subplot(412)
data1 = np.genfromtxt("count_abnormal.txt")
data2 = np.genfromtxt("count_abnormal_train.txt")
pl.plot(data1/184.0,linewidth=0.7,color='green',label='Validating Accuracy')
pl.plot(data2/24760.0,linewidth=0.7,color='red',label='Training Accuracy')
pl.axvline(17,color='k',linewidth=0.5,linestyle="--")
pl.title("Accuracy Rate of Abnormal Recognition Varies with Training Epochs")
pl.xlabel('Epoch')
pl.legend()

pl.subplot(413)
# pl.plot(data1/184.0,linewidth=0.7,color='green',label='Validating Accuracy')
data0 = np.genfromtxt('count_abnormal.txt')
data = np.copy(data0)
data = data * (5184.0-184.0)/184.0
data1 = np.genfromtxt('count.txt')
data_normal = 5000.0*np.ones(data.shape[0])
pl.plot(data/(data+(data_normal-(data1-data0))),linewidth=0.7,color='orange',label='Validating Precision')
pl.title("Normalized-Precision of Abnormal Recognition Varies with Training Epochs")
pl.xlabel('Epoch')
pl.legend()

pl.subplot(414)
data0 = np.genfromtxt('loss in every step training model.txt')
pl.plot(data0,linewidth=0.7,color='blue',label='Loss')
pl.title("Loss Varies with Training Epochs")
pl.xlabel('Epoch')
pl.legend()

pl.subplots_adjust(hspace=0.4)
pl.tight_layout()

pl.savefig("fig.png")
