import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = 'timeStd_Max_within_2Hours_per_SpacePoint.txt'
    data = np.genfromtxt(path)
    data = np.array(data)
    print data.shape

#    subdata = data[11:12,:]
#    print subdata.shape
    subdata = data.max(1)
    print subdata.shape

    subdata = np.transpose(subdata)
    print subdata.shape

    max_sub = max(subdata)
    print max_sub
    subdata = subdata/max_sub

    fig = plt.figure()
    plt.bar(np.arange(12), subdata, 0.4, color='green')
    plt.xlabel('Time Segment Number')
    plt.ylabel('2HoursStdMax-among-allSpacePoints / V')
#    plt.title('StdMax Within 22 To 24')
#    plt.plot(np.arange(0, 46986, 2), subdata, color='orange')
    plt.show()
