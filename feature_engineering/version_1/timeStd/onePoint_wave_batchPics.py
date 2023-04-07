import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = 'timeStd_Max_within_2Hours_per_SamplePoint.txt'
    data = np.genfromtxt(path)
    data = np.array(data)
    for i in np.arange(47):
        data1 = data[:,i:i+1]
        max_data = max(data1)
        data1 = data1/max_data
        plt.plot(np.arange(12), data1, color='brown')
        plt.xlabel('Time Segment Number')
        plt.ylabel('2HoursStdMax / V')
        plt.title('Wave Plot of Space Point at ' + str(i) + ' kms')
#        plt.savefig('onePointWave/Wave Plot of Space Point at ' + str(i) + ' kms.jpg')
        plt.show()
