import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy.signal import convolve2d
import matplotlib

img = plt.imread('uniandes.png')
#print np.shape(img)

t = np.linspace(-10, 10, 20)
bump = np.exp(-0.05*(t**2))
bumb = bump / np.trapz(bump)
kernel = bump[:, np.newaxis] * bump[np.newaxis, :]
kernel_ft = fftpack.fft2(kernel, shape = img.shape[:2], axes = (0, 1))
img_ft = fftpack.fft2(img, axes=(0, 1))
img2_ft = kernel_ft[:, :, np.newaxis]*img_ft
img2 = fftpack.ifft2(img2_ft, axes=(0,1)).real
fig = plt.figure(1, figsize=(9.5,9))
plt.imsave('uniandes2.png', img2)
print kernel

#print matplotlib.__version__ 
#print np.__version__
#print img 
