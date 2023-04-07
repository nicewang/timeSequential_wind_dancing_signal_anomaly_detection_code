from travel_path import *
import pylab as pl

path = "freq_models/"
files = travel_txt(path)
list_files(files)

pl.figure(figsize=(12,8))
freqs = np.linspace(0,1.0,601)
for i in range(files.shape[0]):
    data = np.genfromtxt(files[i])
    pl.subplot(2,3,i+1)
    pl.plot(freqs,data)
    pl.xlabel(u'Freq / Hz')
    pl.ylabel(u'Amplitude / V')
    pl.title(u'('+str(i+1)+u')')

pl.subplots_adjust(hspace=0.3)
pl.savefig(u"plot of freq models.png")