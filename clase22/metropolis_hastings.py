import numpy as np
import matplotlib.pyplot as plt

n_iteraciones = 200000

#funcion

def nasty_function(x):
	return np.exp(-(x**2))/((x-3.0)*(x-3.0) + 0.01*0.01)

#inicializacion

x_walk = []
x_0 = 8.0*(np.random.random()-0.5)
x_walk = np.append(x_walk, x_0)

#iteracion del metodo

for i in range(0, n_iteraciones):
	x_new = np.random.normal(x_walk[i], 1.0)
	alpha = nasty_function(x_new)/nasty_function(x_walk[i])
	if(alpha > 1):
		x_walk = np.append(x_walk, x_new)
	else:
		beta = np.random.random()
		if(alpha > beta):
			x_walk = np.append(x_walk, x_new)
		else:
			x_walk = np.append(x_walk, x_walk[i])

x = np.linspace(-4.0, 4.0, 3000)			
f = nasty_function(x)
norm = np.sum(f*(x[1]-x[0]))
plt.plot(x, f/norm, linewidth = 1, color = "r")
plt.hist(x_walk, 1000, normed = True)
plt.show()
