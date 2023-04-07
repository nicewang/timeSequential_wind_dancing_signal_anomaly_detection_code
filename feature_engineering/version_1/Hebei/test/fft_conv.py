import numpy as np

def fft_convolve(a,b):
    n = len(a) + len(b) - 1
    N = 2**(int(np.log2(n))+1)
    A = np.fft.fft(a, N)
    B = np.fft.fft(b, N)
    return np.fft.ifft(A*B)[:n]

a = np.random.rand(128)
b = np.random.rand(128)
c = np.convolve(a,b)

print np.sum(np.abs(c - fft_convolve(a,b)))
