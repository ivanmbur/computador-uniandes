import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc("text", usetex = True)

n_x = 80
x = np.linspace(0, 2.0, n_x)
r = 0.5
dx = x[1]-x[0]
c = 1.0
dt = r*dx/c
n_t = int(0.3/dt)
u = np.zeros((len(x)))
u[np.where((x<1.25)&(x>0.75))] = 1
u_inicial = u
for n in range(n_t):
	u_past = u.copy()
	for i in range(1,n_x-1):
		u[i]=u_past[i]-r*(u_past[i]-u_past[i-1])
u_lineal = u.copy()
u = u_inicial
u = np.zeros((len(x)))
u[np.where((x<1.25)&(x>0.75))] = 1
for n in range(n_t):
	u_past = u.copy()
	for i in range(1,n_x):
		u[i]=u_past[i]-u_past[i]*r*(u_past[i]-u_past[i-1])
u_no_lineal = u
fig,ax=plt.subplots(2)
ax[0].plot(x, u_lineal)
ax[1].plot(x, u_no_lineal)
plt.show()
