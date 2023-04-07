import sys
import os
import numpy as np

path = sys.argv[1]
data = np.genfromtxt(path)
data = np.array(data)

count = 0
for i in xrange(50, 14000, 1500):
    data1 = data[:, i:i + 1]
    if count == 0:
        data_0km100 = data1
        count = count + 1
        continue
    if count == 1:
        data_3km100 = data1
        count = count + 1
        continue
    if count == 2:
        data_6km100 = data1
        count = count + 1
        continue
    if count == 3:
        data_9km100 = data1
        count = count + 1
        continue
    if count == 4:
        data_12km100 = data1
        count = count + 1
        continue
    if count == 5:
        data_15km100 = data1
        count = count + 1
        continue
    if count == 6:
        data_18km100 = data1
        count = count + 1
        continue
    if count == 7:
        data_21km100 = data1
        count = count + 1
        continue
    if count == 8:
        data_24km100 = data1
        count = count + 1
        continue
    if count == 9:
        data_27km100 = data1
        count = 0
        continue


print '0.1km:'
if os.path.exists('SpacePoint/0.1km/timeStd_of_Point_at_0.1km.txt'):
    data1 = np.genfromtxt('SpacePoint/0.1km/timeStd_of_Point_at_0.1km.txt')
    data_new_2 = np.column_stack((data1, data_0km100))
    print data_new_2
    print data_new_2.shape
    np.savetxt('SpacePoint/0.1km/timeStd_of_Point_at_0.1km.txt', data_new_2)
else:
    print data_0km100
    print data_0km100.shape
    np.savetxt('SpacePoint/0.1km/timeStd_of_Point_at_0.1km.txt', data_0km100)

print '3.1km:'
if os.path.exists('SpacePoint/3.1km/timeStd_of_Point_at_3.1km.txt'):
    data1 = np.genfromtxt('SpacePoint/3.1km/timeStd_of_Point_at_3.1km.txt')
    data_new_2 = np.column_stack((data1, data_3km100))
    print data_new_2
    print data_new_2.shape
    np.savetxt('SpacePoint/3.1km/timeStd_of_Point_at_3.1km.txt', data_new_2)
else:
    print data_3km100
    print data_3km100.shape
    np.savetxt('SpacePoint/3.1km/timeStd_of_Point_at_3.1km.txt', data_3km100)

print 'timeSeg:'
if os.path.exists('SpacePoint/timeSeg/timeStd_of_Point_at_6.1km.txt'):
    data1 = np.genfromtxt('SpacePoint/timeSeg/timeStd_of_Point_at_6.1km.txt')
    data_new_2 = np.column_stack((data1, data_6km100))
    print data_new_2
    print data_new_2.shape
    np.savetxt('SpacePoint/timeSeg/timeStd_of_Point_at_6.1km.txt', data_new_2)
else:
    print data_6km100
    print data_6km100.shape
    np.savetxt('SpacePoint/timeSeg/timeStd_of_Point_at_6.1km.txt', data_6km100)

print '9.1km:'
if os.path.exists('SpacePoint/9.1km/timeStd_of_Point_at_9.1km.txt'):
    data1 = np.genfromtxt('SpacePoint/9.1km/timeStd_of_Point_at_9.1km.txt')
    data_new_2 = np.column_stack((data1, data_9km100))
    print data_new_2
    print data_new_2.shape
    np.savetxt('SpacePoint/9.1km/timeStd_of_Point_at_9.1km.txt', data_new_2)
else:
    print data_9km100
    print data_9km100.shape
    np.savetxt('SpacePoint/9.1km/timeStd_of_Point_at_9.1km.txt', data_9km100)

print '12.1km:'
if os.path.exists('SpacePoint/12.1km/timeStd_of_Point_at_12.1km.txt'):
    data1 = np.genfromtxt('SpacePoint/12.1km/timeStd_of_Point_at_12.1km.txt')
    data_new_2 = np.column_stack((data1, data_12km100))
    print data_new_2
    print data_new_2.shape
    np.savetxt('SpacePoint/12.1km/timeStd_of_Point_at_12.1km.txt', data_new_2)
else:
    print data_12km100
    print data_12km100.shape
    np.savetxt('SpacePoint/12.1km/timeStd_of_Point_at_12.1km.txt', data_12km100)

print '15.1km:'
if os.path.exists('SpacePoint/15.1km/timeStd_of_Point_at_15.1km.txt'):
    data1 = np.genfromtxt('SpacePoint/15.1km/timeStd_of_Point_at_15.1km.txt')
    data_new_2 = np.column_stack((data1, data_15km100))
    print data_new_2
    print data_new_2.shape
    np.savetxt('SpacePoint/15.1km/timeStd_of_Point_at_15.1km.txt', data_new_2)
else:
    print data_15km100
    print data_15km100.shape
    np.savetxt('SpacePoint/15.1km/timeStd_of_Point_at_15.1km.txt', data_15km100)

print '18.1km:'
if os.path.exists('SpacePoint/18.1km/timeStd_of_Point_at_18.1km.txt'):
    data1 = np.genfromtxt('SpacePoint/18.1km/timeStd_of_Point_at_18.1km.txt')
    data_new_2 = np.column_stack((data1, data_18km100))
    print data_new_2
    print data_new_2.shape
    np.savetxt('SpacePoint/18.1km/timeStd_of_Point_at_18.1km.txt', data_new_2)
else:
    print data_18km100
    print data_18km100.shape
    np.savetxt('SpacePoint/18.1km/timeStd_of_Point_at_18.1km.txt', data_18km100)

print '21.1km:'
if os.path.exists('SpacePoint/21.1km/timeStd_of_Point_at_21.1km.txt'):
    data1 = np.genfromtxt('SpacePoint/21.1km/timeStd_of_Point_at_21.1km.txt')
    data_new_2 = np.column_stack((data1, data_21km100))
    print data_new_2
    print data_new_2.shape
    np.savetxt('SpacePoint/21.1km/timeStd_of_Point_at_21.1km.txt', data_new_2)
else:
    print data_21km100
    print data_21km100.shape
    np.savetxt('SpacePoint/21.1km/timeStd_of_Point_at_21.1km.txt', data_21km100)

print '24.1km:'
if os.path.exists('SpacePoint/24.1km/timeStd_of_Point_at_24.1km.txt'):
    data1 = np.genfromtxt('SpacePoint/24.1km/timeStd_of_Point_at_24.1km.txt')
    data_new_2 = np.column_stack((data1, data_24km100))
    print data_new_2
    print data_new_2.shape
    np.savetxt('SpacePoint/24.1km/timeStd_of_Point_at_24.1km.txt', data_new_2)
else:
    print data_24km100
    print data_24km100.shape
    np.savetxt('SpacePoint/24.1km/timeStd_of_Point_at_24.1km.txt', data_24km100)

print '27.1km:'
if os.path.exists('SpacePoint/27.1km/timeStd_of_Point_at_27.1km.txt'):
    data1 = np.genfromtxt('SpacePoint/27.1km/timeStd_of_Point_at_27.1km.txt')
    data_new_2 = np.column_stack((data1, data_27km100))
    print data_new_2
    print data_new_2.shape
    np.savetxt('SpacePoint/27.1km/timeStd_of_Point_at_27.1km.txt', data_new_2)
else:
    print data_27km100
    print data_27km100.shape
    np.savetxt('SpacePoint/27.1km/timeStd_of_Point_at_27.1km.txt', data_27km100)
