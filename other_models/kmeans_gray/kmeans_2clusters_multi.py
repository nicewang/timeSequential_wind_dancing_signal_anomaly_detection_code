# -*- coding: utf-8 -*-
import cv2
from travel_path import *

freqStd_files = travel_txt("freqStd/")

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

for i in range(freqStd_files.shape[0]):
    SpacePoint = freqStd_files[i].split(' ')[-1]
    SpacePoint = SpacePoint.split('.')[0] + '.' + SpacePoint.split('.')[1] + '.' + SpacePoint.split('.')[-1]
    print(SpacePoint)

    data = np.genfromtxt(freqStd_files[i])
    data_multi = []
    for j in range(data.shape[0]):
        if data_multi == []:
            data_multi = data[j,0] * data[j,1]
        else:
            data_tmp = data[j,0] * data[j,1]
            data_multi = np.column_stack((data_multi, data_tmp))
    data_multi = np.float32(data_multi)
    # k聚类
    ret, label, center = cv2.kmeans(data_multi, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    print(label.shape)

    suffix = np.array([[0],[1]])
    center = np.column_stack((center, suffix))
    print(center)
    for j in range(2):
        for k in range(j+1,2):
            if center[j,0] > center[k,0]:
                tmp1 = np.copy(center[k,:])
                tmp2 = np.copy(center[j,:])
                center[j,:] = tmp1
                center[k,:] = tmp2
    print(center)

    print(label)
    label1 = np.copy(label)
    for j in range(label.shape[0]):
        for k in range(2):
            if label[j,0] == center[k,1]:
                label1[j,0] = np.copy(k)
    print(label1)

    data_new = np.column_stack((data, label1))
    print(data_new.shape)
    np.savetxt("cluster_freqXstd/2 clusters of point at " + SpacePoint, data_new)
