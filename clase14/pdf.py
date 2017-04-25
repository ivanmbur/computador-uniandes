import numpy as np
import matplotlib.pyplot as plt

n_points_x = 1000
x = np.linspace(0.0, 1.0, n_points_x)
u_initial = np.exp(-(x-0.3)**2/0.01)
r = 0.3
dx = x[1] - x[0]
dt = r*dx
n_points_t = 1000
t = np.linspace(0.0, (n_points_t-1)*dt, n_points_t)
u_initial[0] = 0.0
u_initial[n_points_x-1] = 0.0 
u = np.zeros((n_points_t, n_points_x))
u[0,:] = u_initial
u[1,:] = 0
u[1, n_points_x-1] = 0
for i in range(1,n_points_x-1):
	u[1,i] = u[0,i] + r*r*(u[0,i+1]-2*u[0,i]+u[0,i-1])/2
for i in range(2, n_points_t):
	u[i,0] = 0
	u[i,n_points_x-1] = 0
	for j in range(1, n_points_x-1):
		u[i,j] = 2*(1-r*r)*u[i-1,j] - u[i-2,j] + r*r*(u[i-1,j+1]+u[i-1,j-1])
for i in [0, 250, 500, 750,  800, 999]:
	plt.plot(x, u[i,:])
plt.show()
