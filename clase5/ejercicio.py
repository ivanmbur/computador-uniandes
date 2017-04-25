import numpy as np
import matplotlib.pyplot as plt

def f(E):
	return (np.sqrt(10 - E) * np.tan(np.sqrt(10 - E))) - np.sqrt(abs(E))

def f_prime(E, h):
	return (f(E + h) - f(E - h))/(2*h)

x = np.linspace(4, 10, 1000)
plt.plot(x, f(x))
plt.show()

guess = 7.5
h = 0.001
while (abs(f(guess)) > 0.001):
	delta = -f(guess)/f_prime(guess,h)
	guess = guess + delta
	print guess
