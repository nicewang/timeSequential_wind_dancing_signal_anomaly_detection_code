import glob
import os
import numpy as np

def travel_txt(path):
    files = []
    for file in glob.glob(path+'/*.txt'):
        files.append(file)
    return np.asarray(files)

def travel_txt_in_path(path):
    cate = [path+x for x in os.listdir(path) if os.path.isdir(path+x)]
    files = []
    for idx,folder in enumerate(cate):
        for file in glob.glob(folder+'/*.txt'):
            files.append(file)
    return np.asarray(files)

def list_files(files):
    for i in range(files.shape[0]):
        print(files[i])
