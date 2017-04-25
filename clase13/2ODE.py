import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc("text", usetex = True)

dx = 0.01
min_x = 0.0
max_x = 6.0
n_points = int((max_x-min_x)/dx)
x = np.zeros(n_points)
y = np.zeros((n_points,2))

def f_prime(x, y):
	return np.array([y[1], -4*y[0]])

x[0] = min_x
y[0] = np.array([1, 0])

for i in range(1, n_points):
	x[i] = x[i-1] + dx
	y[i] = y[i-1] + dx*f_prime(x[i-1],y[i-1])

fig, ax = plt.subplots(2, sharex = True)
ax[0].plot(x, y[:,0], "ko", label = "Euler")
ax[0].plot(x, np.cos(2.0*x), label = "Verdadera")
ax[1].plot(x, np.cos(2.0*x)-y[:,0], "ko", label = "Error")
ax[1].set_xlabel("$x$")
ax[0].set_ylabel("$y$")
ax[1].set_ylabel("$y_{\mathrm{true}} - y_{\mathrm{euler}}$")
ax[0].legend()
ax[0].set_title(r"M\'etodo de Euler")

def f_prime_4(x,y):
	k_1 = f_prime(x,y)
	k_2 = f_prime(x+dx/2,y + k_1*dx/2)
	k_3 = f_prime(x+dx/2,y + k_2*dx/2)
	k_4 = f_prime(x+dx, y + k_3*dx)
	return (k_1 + 2*k_2 + 2*k_3 + k_4)/6

x[0] = min_x
y[0] = np.array([1, 0])

for i in range(1, n_points):
	x[i] = x[i-1] + dx
	y[i] = y[i-1] + dx*f_prime_4(x[i-1],y[i-1])

fig, ax = plt.subplots(2, sharex = True)
ax[0].plot(x, y[:,0], "ko", label = "Runge-kutta 4")
ax[0].plot(x, np.cos(2.0*x), label = "Verdadera")
ax[1].plot(x, np.cos(2.0*x)-y[:,0], "ko", label = "Error")
ax[1].set_xlabel("$x$")
ax[0].set_ylabel("$y$")
ax[1].set_ylabel("$y_{\mathrm{true}} - y_{\mathrm{runge}}$")
ax[0].legend()
ax[0].set_title(r"Runge-kutta 4th order")

plt.show()

