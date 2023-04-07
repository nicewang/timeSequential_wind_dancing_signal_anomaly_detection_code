import numpy as np
import datetime

time1 = datetime.datetime.now()
for i in xrange(1000):
    i_ = i
time2 = datetime.datetime.now()
print "Time diff of xrange:"
print time2-time1

time3 = datetime.datetime.now()
for i in np.arange(1000):
    i_ = i
time4 = datetime.datetime.now()
print "Time diff of np arange:"
print time4-time3
