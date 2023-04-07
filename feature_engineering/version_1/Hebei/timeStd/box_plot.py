import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = 'timeStd_2017061523.txt'
    data = np.genfromtxt(path)
    data = np.array(data)

    print data.shape

    data_sample_30 = []
    for i in xrange(0, 15000, 500):
        data1 = data[:, i:i + 1]
        if data_sample_30 == []:
            data_sample_30 = data1
        else:
            data_sample_30 = np.column_stack((data_sample_30, data1))

    index_sample = np.arange(30)
    df_sample_50 = pd.DataFrame(data_sample_30, columns=index_sample)

    df = pd.DataFrame(data)

    df_sample_50.boxplot()
#    df.boxplot()

    plt.xlabel('Distance between Sample Point and Start Point / km')
    plt.ylabel('Waving Amplitude / V')
#    plt.title('Box Plot of Waving Amplitude of All Points in 32.5-to-33.5km within 24 Hours')
    plt.title('Box Plot of Waving Amplitude of 50 Sample Points - 20170615_23_24')

    plt.show()
