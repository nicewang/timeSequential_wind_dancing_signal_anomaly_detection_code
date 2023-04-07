from numpy.fft import *
from matplotlib.pyplot import *
import numpy as np

# create a wave with 1Mhz and 0.5Mhz frequencies
dt = 2e-9
t = np.arange(0, 10e-6, dt)
y = np.cos(2 * np.pi * 1e6 * t) + (np.cos(2 * np.pi * 2e6 *t) * np.cos(2 * np.pi * 2e6 * t))
y *= np.hanning(len(y))
yy = np.concatenate((y, ([0] * 10 * len(y))))

# FFT of this
Fs = 1 / dt  # sampling rate, Fs = 500MHz = 1/2ns
n = len(yy)  # length of the signal
k = np.arange(n)
T = n / Fs
frq = k / T  # two sides frequency range
frq = frq[range(n / 2)]  # one side frequency range
Y = fft(yy) / n  # fft computing and normalization
Y = Y[range(n / 2)] / max(Y[range(n / 2)])

# plotting the data
subplot(2, 2, 1)
plot(t * 1e3, y, 'r')
xlabel('Time (micro seconds)')
ylabel('Amplitude')
grid()

# plotting the spectrum
subplot(2, 2, 2)
plot(frq[0:600], abs(Y[0:600]), 'k')
xlabel('Freq (Hz)')
ylabel('|Y(freq)|')
grid()

# plotting the specgram
subplot(2, 2, 3)
Pxx, freqs, bins, im = specgram(y, NFFT=512, Fs=Fs, noverlap=10)
show()