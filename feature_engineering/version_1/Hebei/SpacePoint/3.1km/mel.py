from scikits.talkbox.features import mel
import numpy as np
import pylab as pl

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)

fs = data.shape[0]
fs = fs / (24*3600.0)

sampling_rate = fs
fft_size = data.shape[0]

t0 = np.arange(0, 24.0, 24.0/data_o.shape[0])

t = np.arange(0, 24.0, 24.0/fft_size)
xs = data

xf = np.fft.rfft(xs)
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1)
data_fft = np.clip(np.abs(xf), 1e-20, 1e100)
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
xfp1 = 20*np.log10(np.clip(np.abs(xf/fft_size), 1e-20, 1e100))

data_hz2mel = mel.hz2mel(data_fft)
data_mel2hz = mel.mel2hz(data_hz2mel)

pl.figure(figsize=(10,8))

pl.subplot(421)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(422)
pl.plot(freqs, data_fft)
pl.title(u"Frequency")

pl.subplot(423)
pl.plot(freqs, data_hz2mel)
pl.title(u"Mel Frequency")

pl.subplot(424)
pl.plot(freqs, data_mel2hz)
pl.title(u"Mel Frequency Back")

pl.subplot(425)
pl.plot(freqs, xfp)
pl.title(u"Frequency (dB) 1")

pl.subplot(426)
pl.plot(freqs, xfp1)
pl.title(u"Frequency (dB) 2")

pl.subplots_adjust(hspace=0.4)
pl.show()

print np.log(10)
print np.log10(10)
print 1127.01048*np.log(10)
