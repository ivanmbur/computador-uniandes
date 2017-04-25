import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)

number = 10000
random = np.random.rand(number, 2)*2 - 1
counter = 0.0
for sample in random:
	if (sample[0]**2 + sample[1]**2 < 1):
		counter += 1
pi = 4*counter/number

print "pi es %f" % pi

def f(x):
	return np.exp(-x)

random = np.random.random(number)
integral = np.mean(f(random))
print "Promedio por motecarlo es %f" % integral

x = np.linspace(0, 1, number)
random = np.random.rand(number, 2)
plt.plot(x, f(x))
plt.scatter(random[:,0], random[:,1], alpha = 0.1)
posiciones = np.where(random[:,1] < f(random[:,0]))
plt.scatter(random[posiciones][:,0], random[posiciones][:,1], alpha = 0.2)
plt.show()

integral = float(len(random[posiciones][:,0]))/number
print "Area por montecarlo es %f" % integral
