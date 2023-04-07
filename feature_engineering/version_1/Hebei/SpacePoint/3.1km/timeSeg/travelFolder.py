import numpy as np
import glob

def travel_txt(path):
    texts = []
    for text in glob.glob(path+'*.txt'):
        texts.append(text)
    return np.asarray(texts)

def list_files(files):
    for i in xrange(files.shape[0]):
        print files[i]
