from subprocess import call
import numpy as np

for i in np.arange(13):
    call("python mfcc.py "+str(i), shell=True)
