import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("movimiento.dat")

G = np.zeros((len(datos[:,0]), 3))
for i in range(0,len(datos[:,0])):
	G[i][0] = 1
	G[i][1] = datos[i][0]
	G[i][2] = datos[i][0]**2 * 0.5
GT = np.transpose(G)
sol = np.linalg.solve(np.dot(GT,G),np.dot(GT,datos[:,1]))

T = np.linspace(0, 10, 1000) 
plt.scatter(datos[:,0],datos[:,1])
plt.plot(T, sol[0] + sol[1]*T + sol[2]*0.5*T**2)
plt.show()
