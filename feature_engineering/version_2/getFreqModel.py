# -*- coding: utf-8 -*-
import numpy as np

path = "original_onePointData/Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data = np.diff(data)

i = 1132
sub_data = data[100*i-550:100*(i+1)+550]
# 进行快速傅立叶变换
xf = np.fft.rfft(sub_data)
xf = np.abs(xf)
xf = xf / max(xf)

np.savetxt('freq_models/freq model1 of 3.1km-1132.txt',xf)