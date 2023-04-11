# -*- coding: utf-8 -*-
import cv2
from travel_path import *
import math

# calculate Euclidean distance
def euclDistance(vector1, vector2):
    return math.sqrt(sum(pow(vector2 - vector1, 2)))

freqStd_files = travel_txt("freqStd/")

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

for i in range(freqStd_files.shape[0]):
    SpacePoint = freqStd_files[i].split(' ')[-1]
    SpacePoint = SpacePoint.split('.')[0] + '.' + SpacePoint.split('.')[1] + '.' + SpacePoint.split('.')[-1]
    print(SpacePoint)

    data = np.genfromtxt(freqStd_files[i])
    data_1 = data
    data_1 = np.float32(data_1)
    # k聚类
    ret, label, center = cv2.kmeans(data_1, 3, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    print(label.shape)

    suffix = np.array([[0],[1],[2]])
    center = np.column_stack((center, suffix))
    print(center)
    for j in range(3):
        for k in range(j+1,3):
            vec0 = np.array([0, 0])
            vec1 = center[j, :2]
            vec2 = center[k, :2]
            if euclDistance(vec1, vec0) > euclDistance(vec2, vec0):
                tmp1 = np.copy(center[k,:])
                tmp2 = np.copy(center[j,:])
                center[j,:] = tmp1
                center[k,:] = tmp2
    print(center)

    print(label)
    label1 = np.copy(label)
    for j in range(label.shape[0]):
        for k in range(3):
            if label[j,0] == center[k,2]:
                label1[j,0] = np.copy(k)
    print(label1)

    data_new = np.column_stack((data, label1))
    print(data_new.shape)
    np.savetxt("cluster_freqStd/3clusters/3 clusters of point at " + SpacePoint, data_new)
