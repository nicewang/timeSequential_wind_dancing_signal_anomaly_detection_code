import numpy as np
import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':
    path = sys.argv[1]
    data = np.genfromtxt(path)
    data = np.array(data)
    data = np.transpose(data)
    data = data.reshape(72 * 24)

    plt.plot(np.arange(0, 24, 24.0/(72*24)), data, color='blue')
    plt.xlabel('Time / Hour')
    plt.ylabel('TimeMean of Waving Signal within 50s / V')
    plt.title('Wave Plot of Space Point at ' + str(path).split('_')[4].split('.')[0] + '.' + str(path).split('_')[4].split('.')[1])
    title = 'Wave Plot of Space Point at ' + str(path).split('_')[4].split('.')[0] + '.' + str(path).split('_')[4].split('.')[1]
    title = title + '.jpg'
    title = 'pic/' + title
    print title
    plt.savefig(title)
