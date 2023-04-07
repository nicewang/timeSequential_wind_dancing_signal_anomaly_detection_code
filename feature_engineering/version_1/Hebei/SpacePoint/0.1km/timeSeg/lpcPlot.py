# -*- coding: utf-8 -*-
from travelFolder import *
import numpy as np
import pylab as pl
from scikits.talkbox.linpred import py_lpc
from sklearn.preprocessing import PolynomialFeatures

path = ''
files = travel_txt(path)
list_files(files)

pl.figure(figsize=(24,36))

for i in np.arange(files.shape[0]):

    if i < 2:
        i_ = i
    elif i < 12:
        i_ = i - 2 + 10
    elif i == 12:
        i_ = 2
    elif i < 17:
        i_ = i - 13 + 20
    else:
        i_ = i - 17 + 3

    data = np.genfromtxt(files[i])
    data = np.array(data)
    data = np.diff(data)

    data_lpc = []
    for j in np.arange(120):
        data_sub = data[60*j:60*(j+1)]
        data_sub = py_lpc.lpc_ref(data_sub,10)
        data_sub = data_sub[1:]
        if data_lpc == []:
            data_lpc = data_sub
        else:
            data_lpc = np.row_stack((data_lpc, data_sub))
    data_lpc = data_lpc.mean(1)

    data_lpc = data_lpc.reshape(data_lpc.shape[0], 1)

    poly4 = PolynomialFeatures(4)
    featureSelection4 = poly4.fit_transform(data_lpc)

    t = np.arange(i_, i_+1, 1.0 / data_lpc.shape[0])

    pl.subplot(8,3,i_+1)
    pl.plot(t, data_lpc, color='blue')
    #pl.plot(t, featureSelection4)
    pl.title(u"10-LPC Coefficients Average of Diff Data within "+str(i_)+u"-"+str(i_+1)+" (Point at 0.1km)")
    #pl.title(u"Polynomial Features of 10-LPC Coefficients Average within " + str(i_) + u"-" + str(i_ + 1) + " (Point at 0.1km)")

pl.subplots_adjust(hspace=0.6)
pl.savefig(u"10-LPC Coefficients Average of Diff Data of Point at 0.1km.jpg")
#pl.savefig(u"Polynomial Features of 10-LPC Coefficients Average of Diff Data of Point at 0.1km.jpg")
