import numpy as np
import matplotlib.pyplot as plt

n = 128
f = 200.0
dt = 1/(f*32)
t = np.linspace(0, (n-1)*dt, n)
y = np.cos(2*np.pi*f*t)

#plt.plot(t,y)
#plt.plot(t,y, "ko")
#plt.show()

y = np.cos(2*np.pi*f*t) - 0.4*np.sin(2*np.pi*2*f*t)

#plt.plot(t,y)
#plt.plot(t,y, "ko")
#plt.show()

from scipy.fftpack import fft, fftfreq
fft_x = fft(y)/n
freq = fftfreq(n,dt)
#plt.plot(freq,abs(fft_x))
#plt.show()

#fft_x_shifted = np.fft.fftshift(fft_x)
#freq_shifted = np.fft.fftshift(freq)
#plt.plot(freq_shifted, np.abs(fft_x_shifted))
#plt.xlim(0,1000)
#plt.show()

half_n = int(np.ceil(n/2.0))
fft_x_half = (2.0) * fft_x[:half_n]
freq_half = freq[:half_n]
#plt.plot(freq_half, np.abs(fft_x_half))
#plt.show()
