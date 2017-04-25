import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.exp(-(x**2))
def f_prime(x):
	return -2*x*np.exp(-(x**2))

n_points = 1000
x = np.linspace(-5.0, 5.0, n_points)
h = x[1] - x[0]
print h
y = f(x)
plt.plot(x,y)
plt.show()

f_prime_diff = (y[1:] - y[0:-1])/h
f_prime_true = f_prime(x[0:-1])
f_prime_diff_central = (y[2:] - y[0:-2])/(2*h)
f_prime_true_central = f_prime(x[1:-1])
plt.scatter(x[0:-1], f_prime_diff, s = 0.1, c = "k")
plt.scatter(x[1:-1], f_prime_diff_central, s = 0.1, c = "g")
plt.plot(x[0:-1], f_prime_true)
plt.plot(x[1:-1], f_prime_true_central)
plt.show()

plt.plot(x[0:-1], abs(f_prime_true - f_prime_diff))
plt.plot(x[1:-1], abs(f_prime_true_central - f_prime_diff_central))
plt.show()

plt.plot(x[0:-1], abs(f_prime_true - f_prime_diff)/h)
plt.plot(x[1:-1], abs(f_prime_true_central - f_prime_diff_central)/(h*h))
plt.show()
