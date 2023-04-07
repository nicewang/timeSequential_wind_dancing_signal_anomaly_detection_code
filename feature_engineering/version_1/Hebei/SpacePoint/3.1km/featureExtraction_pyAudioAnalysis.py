from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
import numpy as np

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)

fs = data.shape[0]
fs = fs / (24*3600.0)

fft_size = data.shape[0]

t = np.arange(0, 24.0, 24.0/fft_size)

F = audioFeatureExtraction.stFeatureExtraction(data, 16000, 1024, 256)

zcr = np.array(F[0,:])
print zcr.shape

energy = np.array(F[1,:])
print energy.shape

energy_entropy = np.array(F[2,:])
print energy_entropy.shape

plt.figure(figsize=(8,8))

plt.subplot(411)
plt.plot(t, data)
plt.title(u"Original Diff Data")
plt.xlabel(u"Time / h")
plt.ylabel(u"Amplitude / V")

plt.subplot(4,1,2)
plt.plot(F[0,:], label=u"frame_len=512s,hop_len=128s")
plt.xlabel('Frame no')
plt.ylabel('ZCR')
plt.legend()

plt.subplot(4,1,3)
plt.plot(F[1,:], label=u"frame_len=512s,hop_len=128s")
plt.xlabel('Frame no')
plt.ylabel('Energy')
plt.legend()

plt.subplot(4,1,4)
plt.plot(F[2,:], label=u"frame_len=512s,hop_len=128s")
plt.xlabel('Frame no')
plt.ylabel('Energy Entropy')
plt.legend()

plt.subplots_adjust(hspace=0.6)
plt.show()
