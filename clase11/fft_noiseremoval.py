import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

n = 512
f = 200.0
dt = 1 / (f * 128)
t = np.linspace(0,(n-1)*dt,n)
y = np.sin(2*np.pi*f*t) + np.cos(2*np.pi*f*t*t)
noise = 1.4*(np.random.rand(n)+0.7)
y = y + noise
#plt.plot(t, y)
#plt.show()

fft_x = fft(y)
freq = fftfreq(n,dt)
plt.plot(freq,np.abs(fft_x))
plt.show()
