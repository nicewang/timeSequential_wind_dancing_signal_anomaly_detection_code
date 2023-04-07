from librosa.core import spectrum
import librosa.core as core
import numpy as np
import pylab as pl
from librosa.display import *
import librosa
from scipy import signal

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)

fs = data.shape[0]
fs = fs / (24*3600.0)

fft_size = data.shape[0]

t = np.arange(0, 24.0, 24.0/fft_size)

D = core.stft(data)

pl.figure(figsize=(16,8))

pl.subplot(221)
#specshow(librosa.amplitude_to_db(D, ref=np.max), y_axis='log', x_axis='time')
pl.pcolormesh(np.arange(D.shape[1]), np.arange(D.shape[0]), 20*np.log10(np.abs(D)))
pl.title('Power spectrogram')
pl.colorbar(format='%+2.0f dB')
pl.tight_layout()

f, t, Sxx = signal.spectral.spectrogram(data, fs)

pl.subplot(222)
pl.pcolormesh(t, f, 20*np.log10(np.abs(Sxx)))
pl.ylabel('Frequency [Hz]')
pl.xlabel('Time [sec]')
pl.colorbar(format='%+2.0f dB')
pl.tight_layout()

f, t, Zxx = signal.spectral.stft(data, fs)
print t.shape

pl.subplot(223)
pl.pcolormesh(t, f, 20*np.log10(np.abs(Zxx)))
pl.ylabel('Frequency [Hz]')
pl.xlabel('Time [sec]')
pl.colorbar(format='%+2.0f dB')
pl.tight_layout()

pl.show()

if_gram, D = spectrum.ifgram(data,sr=fs)
print if_gram.shape
print D.shape

#specshow(librosa.amplitude_to_db(if_gram, ref=np.max), y_axis='log', x_axis='time')
#specshow(20*np.log10(np.abs(if_gram)), y_axis='log', x_axis='time')
#pl.pcolormesh(np.arange(if_gram.shape[1]), np.arange(if_gram.shape[0]), 20*np.log10(np.abs(if_gram)))
pl.pcolormesh(np.arange(if_gram.shape[1]), np.arange(if_gram.shape[0]), np.abs(if_gram))
pl.title('Power spectrogram')
#pl.colorbar(format='%+2.0f dB')
pl.colorbar()
pl.tight_layout()

pl.show()
