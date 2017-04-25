import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

img = plt.imread("moonlanding.png")
fourier = fftpack.fft2(img, axes = (0,1))
fft = np.log10(abs(fourier)**2)
for i in range(50, len(img) - 50):
	for j in range(0, len(img[0])):
		fourier[i][j] = 0 
for i in range(50, len(img[0]) - 50):
	for j in range(0, len(img)):
		fourier[j][i] = 0
fft_new = np.log10(abs(fourier)**2)
img_new = fftpack.ifft2(fourier, axes = (0,1)).real

fig, ax = plt.subplots(2, 2, figsize = (10, 8))
ax[0,0].imshow(img)
ax[0,0].set_title("Original")
ax[1,0].imshow(img_new)
ax[1,0].set_title("Procesado")
ax[0,1].imshow(fft)
ax[0,1].set_title("FFT Original")
ax[1,1].imshow(fft_new)
ax[1,1].set_title("FFT Procesado")
plt.savefig("moon_landing.png")  
