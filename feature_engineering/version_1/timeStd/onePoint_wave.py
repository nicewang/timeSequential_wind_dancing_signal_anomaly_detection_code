import numpy as np

if __name__ == '__main__':
    path = 'timeStd_Max_within_2Hours_per_SpacePoint.txt'
    data = np.genfromtxt(path)
    data = np.array(data)
    data_sample = data[:,0:1]
    for i in np.arange(500, 23493, 500):
        data1 = data[:,i:i+1]
        data_sample = np.column_stack((data_sample, data1))
    print data_sample.shape
    np.savetxt('timeStd_Max_within_2Hours_per_SamplePoint.txt', data_sample)
