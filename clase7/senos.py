import numpy as np
import matplotlib.pyplot as plt

t = [0, 0.25, 0.5, 0.75]
y = [3, 1, -3, 1]

A = np.zeros((4,4))
for i in range(0,4):
	A[i] = [np.cos(np.pi*t[i]), np.cos(2*np.pi*t[i]), np.cos(3*np.pi*t[i]), np.cos(4*np.pi*t[i])]

sol = np.linalg.solve(A, y)

T = np.linspace(0, 1, 100)
plt.scatter(t, y)
plt.plot(T, sol[0]*np.cos(np.pi*T) + sol[1]*np.cos(2*np.pi*T) + sol[2]*np.cos(3*np.pi*T) + sol[3]*np.cos(4*np.pi*T))
plt.show()
