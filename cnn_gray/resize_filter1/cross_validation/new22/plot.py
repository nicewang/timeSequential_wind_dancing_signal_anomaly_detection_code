import numpy as np
import pylab as pl

pl.figure(figsize=(11,9))

data = np.genfromtxt("loss_acc/acc in every step training model.txt")
data = data[:490]

pl.subplot(221)
pl.plot(data, color='blue')
pl.xlabel('Epoch')
pl.ylabel('Training Accuracy Rate')
pl.title('Training Accuracy Rate Varies with Training Epochs\n'
         + '(Model3, Ratio of Normal and Abnormal is 1:1 in Training Set)')

data = np.genfromtxt("loss_acc/loss in every step training model.txt")
data = data[:490]

pl.subplot(222)
pl.plot(data, color='blue')
pl.xlabel('Epoch')
pl.ylabel('Loss')
pl.title('Loss Varies with Training Epochs\n'
         + '(Model3, Ratio of Normal and Abnormal is 1:1 in Training Set)')

data = np.genfromtxt("validate_acc/count.txt")
data = data[:490]
data_abnormal = np.genfromtxt("validate_acc/count_abnormal.txt")
data_abnormal = data_abnormal[:490]

pl.subplot(223)
pl.plot(data/5184.0, color='k', linewidth=0.7, label='Accuracy in All')
pl.plot(data_abnormal/192.0, color='r', linewidth=0.7, label='Accuracy in Abnormal')
pl.plot((data-data_abnormal)/4992.0, color='b', linewidth=0.7, label='Accuracy in Normal')
pl.xlabel('Epoch')
pl.ylabel('Test Accuracy Rate')
pl.title('Test Accuracy Rate Varies with Training Epochs\n'
         + '(Model3, Ratio of Normal and Abnormal is 1:1 in Training Set)')
pl.legend()

data = np.genfromtxt("validate_acc/count_abnormal.txt")
data = data[:490]
data_new = []
for i in range(data.shape[0]-5+1):
    data_tmp = data[i:i+5]
    data_mean = np.mean(data_tmp,axis=0)
    data_mean = data_mean/192.0
    if data_new == []:
        data_new = np.array([[data_mean]])
    else:
        data_new = np.row_stack((data_new, data_mean))
epochs = np.arange(1,data_new.shape[0]+1)

pl.subplot(224)
pl.plot(epochs,data_new,color='r')
pl.title("Mean of abnormal-testing accuracy rates of" + "\n"
         + "5 classifiers having neighboring training epochs")
pl.xlabel("Training Epochs of 1st Classifier")
pl.ylabel("Abnormal-Testing Accuracy Rates Mean")

pl.tight_layout()

pl.savefig(u'fig.png')
