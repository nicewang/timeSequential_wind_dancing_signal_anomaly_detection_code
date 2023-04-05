import numpy as np
import pylab as pl

data = np.genfromtxt("count_abnormal.txt")
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

pl.plot(epochs,data_new,color='r')
pl.title("Mean of abnormal-testing accuracy rates of" + "\n"
         + "5 classifiers having neighboring training epochs")
pl.xlabel("Training Epochs of 1st Classifier")
pl.ylabel("Abnormal-Testing Accuracy Rates Mean")

print(data_new)

pl.show()