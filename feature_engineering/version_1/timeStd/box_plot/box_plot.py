import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = '20140627_054946CH1.txt'
    data = np.genfromtxt(path)
    data = np.array(data)
    data = np.transpose(data)
    data = np.diff(data)
    data = np.transpose(data)

    data_sample = data[:,5000:5500]

    data_sample_50 = []
    for i in xrange(0, 500, 10):
        data1 = data[:, i:i + 1]
        if data_sample_50 == []:
            data_sample_50 = data1
        else:
            data_sample_50 = np.column_stack((data_sample_50, data1))

    index_sample = np.arange(50)
    df_sample_50 = pd.DataFrame(data_sample_50, columns=index_sample)

    df = pd.DataFrame(data_sample)

    df_sample_50.boxplot()

    plt.xlabel('Sample Point No.')
    plt.ylabel('Waving Amplitude / V')
#    plt.title('Box Plot of Waving Amplitude of All Points from 10km to 11km within 100s - 20140627_054946')
    plt.title('Box Plot of Waving Amplitude of 50 Sample Points in 10-to-11km within 100s - 0m from First Sample Point to Point at 10km - 20140627_054946')
#    plt.title('Box Plot of Waving Amplitude of All Points from 10km to 11km within 100s - 20140627_145022')
#    plt.title('Box Plot of Waving Amplitude of 50 Sample Points in 10-to-11km within 100s - 0m from First Sample Point to Point at 10km - 20140627_145022')

    plt.show()
