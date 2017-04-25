import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

datos_raw = np.loadtxt(open("red3_filtrado.txt", "r"))
longitudes = []
intensidades = []
for line in datos_raw:
	longitudes.append(line[0])
	intensidades.append(line[1])
longitudes = np.array(longitudes)
intensidades = np.array(intensidades)

plt.plot(longitudes, intensidades)
plt.savefig("red3.png", format = "png")

print("La longitud de onda de maxima amplitud es %f nm" % longitudes[np.where(intensidades == np.max(intensidades))])

def gauss(x, a, b, c):
	return a * np.exp(-((x-b)**2)/c)

x = np.linspace(639, 666, 10000)
popt, pcov = curve_fit(gauss, longitudes, intensidades, [10000, 653, 200])
ajuste = gauss(x, popt[0], popt[1], popt[2])

plt.plot(longitudes, intensidades)
plt.plot(x, ajuste)
plt.savefig("red3_fit.png", format = "png")

print("La longitud de onda de maxima amplitud segun el ajuste es %f nm" % x[np.where(ajuste == np.max(ajuste))])
