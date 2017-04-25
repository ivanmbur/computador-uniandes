import numpy as np
import matplotlib.pyplot

#Integrates a function f on the interval [a, b] with a partition of res equal intervals and an approximation of the function of each interval through a polynomial of order n

#def int(a, b, f, res, n):
#	dx = (b - a)/(n*res)
#	x = np.linspace(a, b, n*res)
#	y = f(x)
	
def gauss(x):
	return np.exp(-(x**2))
min_x = -5.0
max_x = 5.0
x = np.linspace(min_x, max_x, 1000)
y = gauss(x)
min_y = 0.0
max_y = np.amax(y)
n_random = 10000
x_random = np.random.rand(n_random) * (max_x - min_x) + min_x
y_random = np.random.rand(n_random) * (max_y - min_y) + min_y
delta = gauss(x_random) - y_random
below = np.where(delta > 0.0)
integral = (max_y - min_y) * (max_x - min_x) * (np.size(below)/(1.0*np.size(y_random)))
print integral
print below
