from numpy import *
import numpy as np

threshold = 50000

# calculate Euclidean distance
def euclDistance(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))


def amplitudeDistance(A0, A1):
    return abs(A0 - A1)


# init centroids with random samples
def initCentroids(dataSet, k):
    numSamples, dim = dataSet.shape
    centroids = zeros((k, dim))
    for i in range(k):
        index = int(random.uniform(0, numSamples))
        centroids[i, :] = dataSet[index, :]
    return centroids


# k-means cluster
def kmeans(threshold, dataSet, k):
    numSamples = dataSet.shape[0]
    # first column stores which cluster this sample belongs to,
    # second column stores the error between this sample and its centroid
    clusterAssment = mat(zeros((numSamples, 2)))
    clusterChanged = True

    ## step 1: init centroids
    centroids = initCentroids(dataSet, k)
    print centroids
    centroids = sort_by_col(centroids, 0)
    print centroids
    if threshold > centroids[k-1, 0]:
        threshold = centroids[k-1, 0]
    print 'init threshold:'
    print threshold

    oo = 0
    while clusterChanged:
        print oo

        clusterChanged = False
        ## for each sample
        for i in xrange(numSamples):
            minDist = 100000.0
            minIndex = 0
            ## for each centroid
            ## step 2: find the centroid who is closest
            for j in range(k):
                distance = amplitudeDistance(centroids[j][0], dataSet[i][0])
#                distance = euclDistance(centroids[j, :], dataSet[i, :])
                if distance < minDist:
                    minDist = distance
                    minIndex = j
                    if j == k-1:
                        if dataSet[i][0] < threshold:
                            threshold = dataSet[i][0]

                    ## step 3: update its cluster
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist

                ## step 4: update centroids
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j, :] = mean(pointsInCluster, axis=0)

        oo += 1

    print 'Congratulations, cluster complete!'
    print 'final threshold:'
    print threshold
    return centroids, clusterAssment

def getClusterTypeArray(clusterAssment, i, j):
    clusterTypeArray = np.zeros([i, j], dtype=np.int8)
    k = 0
    for i1 in range(i):
        for j1 in range(j):
            clusterTypeArray[i1][j1] = int(clusterAssment[k, 0])
            k += 1
    return clusterTypeArray

def sort_by_col(a, col_index):
    a1 = a.T
    col_max = a.shape[-1] - 1

    if col_index < col_max:
        # swap line-col_index and line-col_max
        a1[col_index] = a1[col_index] + a1[col_max]
        a1[col_max] = a1[col_index] - a1[col_max]
        a1[col_index] = a1[col_index] - a1[col_max]

        a2 = np.lexsort(a1)

        # swap line-col_index and line-col_max again
        a1[col_index] = a1[col_index] + a1[col_max]
        a1[col_max] = a1[col_index] - a1[col_max]
        a1[col_index] = a1[col_index] - a1[col_max]
    else:
        a2 = np.lexsort(a1)

    return a[a2]

## step1: load data
print "step 1: load data..."
dataSet = []
data = genfromtxt('timeStd_2017061523.txt')
#data = data[:,4800:5000]
for i in xrange(72):
    for j in xrange(0,15000,1):
        dataSet.append([float(data[i][j]), i, j])

## step 2: clustering...
print "step 2: clustering..."
#dataSet = mat(dataSet)
dataSet = np.array(dataSet)
k = 3
centroids, clusterAssment = kmeans(threshold, dataSet, k)

clusterTypeArray = getClusterTypeArray(clusterAssment, 72, 15000)
print clusterTypeArray
#np.savetxt('2clusters/timeStd_2clusters_23_24.txt', clusterTypeArray)
