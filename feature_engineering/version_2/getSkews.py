import pandas as pd
import numpy as np

def getSkews(path):
    # path = "original_onePointData/Data_of_Point_at_0.1km.txt"
    data = np.genfromtxt(path)
    data = np.diff(data)

    df = []
    for i in range(1727):
        if i == 0:
            df = pd.DataFrame({i: data[100 * i:100 * (i + 1)]})
        else:
            df[i] = data[100 * i:100 * (i + 1)]
    skews = df.skew(axis=0)

    df1 = pd.DataFrame({1727: data[1727 * 100:]})
    skew = df1.skew(axis=0)

    skews[1727] = skew
    skews = np.array(skews)

    return skews
