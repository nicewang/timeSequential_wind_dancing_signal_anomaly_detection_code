from scikits.talkbox.linpred import py_lpc
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

t = np.arange(0, 24.0, 24.0/fft_size)
xs = data

xf = np.fft.rfft(xs)
freqs = np.linspace(0, sampling_rate/2, fft_size/2+1)
data_fft = np.clip(np.abs(xf), 1e-20, 1e100)
xfp = 20*np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
xfp1 = 20*np.log10(np.clip(np.abs(xf/fft_size), 1e-20, 1e100))

print data.shape
lpc_ref = py_lpc.lpc_ref(data, 10)
lpc_ref = lpc_ref[1:]
print lpc_ref
print lpc_ref.mean(0)

lpc_ref_fft = py_lpc.lpc_ref(data_fft, 100)

pl.figure(figsize=(8,6))

pl.subplot(311)
pl.plot(t, data)
pl.title(u"Original Diff Data")

pl.subplot(312)
pl.plot(lpc_ref)
pl.title(u"100 Order LPC(Linear Prediction Coefficients)")

pl.subplot(313)
pl.plot(lpc_ref_fft)
pl.title(u"100 Order LPC(Linear Prediction Coefficients) (fft)")

pl.subplots_adjust(hspace=0.5)
pl.show()
