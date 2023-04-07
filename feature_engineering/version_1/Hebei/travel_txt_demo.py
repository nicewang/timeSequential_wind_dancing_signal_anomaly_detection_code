# -*- coding: utf-8 -*-
import glob
import os
import numpy as np

def travel_txt(path):
    cate = [path+x for x in os.listdir(path) if os.path.isdir(path+x)]
    files = []
    for idx,folder in enumerate(cate):
        for im in glob.glob(folder+'/*.txt'):
            print('reading the images:%s'%(im))
            files.append(im)
    return np.asarray(files)

def list_files(files):
    for i in xrange(files.shape[0]):
        print files[i]
