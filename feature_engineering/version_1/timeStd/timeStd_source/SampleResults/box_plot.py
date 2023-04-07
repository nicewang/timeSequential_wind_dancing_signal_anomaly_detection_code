import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = 'timeStd_SamplePoints_32.5_33.5km.txt'
    data = np.genfromtxt(path)
    data = np.array(data)

    data_sample_50 = []
    for i in xrange(0, 500, 10):
        data1 = data[:, i:i + 1]
        if data_sample_50 == []:
            data_sample_50 = data1
        else:
            data_sample_50 = np.column_stack((data_sample_50, data1))

    index_sample = np.arange(50)
    df_sample_50 = pd.DataFrame(data_sample_50, columns=index_sample)

    df = pd.DataFrame(data)

    df_sample_50.boxplot()
#    df.boxplot()

    plt.xlabel('Sample Point No.')
    plt.ylabel('Waving Amplitude / V')
#    plt.title('Box Plot of Waving Amplitude of All Points in 32.5-to-33.5km within 24 Hours')
    plt.title('Box Plot of Waving Amplitude of 50 Sample Points in 32.5-to-33.5km within 24 Hours - 0m from First Sample Point to Point at 32.5km')

    plt.show()
