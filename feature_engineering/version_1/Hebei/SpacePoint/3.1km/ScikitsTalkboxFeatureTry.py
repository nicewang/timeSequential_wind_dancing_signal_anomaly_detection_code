from scikits.talkbox.linpred import common,levinson_lpc,py_lpc
from scikits.talkbox.spectral import basic
from scikits.talkbox.misc import peak_picking
from scikits.talkbox.transforms import dct,dct_ref
from scikits.talkbox.tools import correlations,ffilter
import numpy as np

path = "Data_of_Point_at_3.1km.txt"
data = np.genfromtxt(path)
data = np.array(data)
data_o = data
data = np.diff(data)

fft_size = data.shape[0]

t = np.arange(0, 24.0, 24.0/fft_size)

levinson_lpc.lpc(data,1)
common.lpcres(data,1)
py_lpc.lpc_ref(data,1)
py_lpc.levinson_1d(data,1)

basic.arspec(data,1)
#basic.periodogram(data)
#basic.taper(data)

peak_picking.find_peaks(data,1)

dct.dctii(data)
dct_ref.direct_dctii(data)
dct_ref.direct_dctii_2(data)

correlations.nextpow2(data)
correlations.acorr(data)
ffilter.slfilter(data)
