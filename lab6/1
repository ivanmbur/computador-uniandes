import numpy as np
import matplotlib.pyplot as plt

m = 0.25
k = 42
mu = 0.15
g = 9.8
T = np.linspace(0, 4, 5000)
dt = T[1] - T[0]
y = np.zeros((len(T), 2))
y[0] = [0.2, 0]

def a(y):
	return -np.sign(y[1])*mu*g - k*y[0]/m

def euler(y):
	y[1] += a(y)*dt
	y[0] += y[1]*dt
	return y

for i in range(1, len(y)):
	y[i] = euler(y[i - 1])

plt.plot(T, y[:, 0])
plt.xlabel("Tiempo (s)")
plt.ylabel("Posicion (m)")
plt.savefig("spring_mass.png")
