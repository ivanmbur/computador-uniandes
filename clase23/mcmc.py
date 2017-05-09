import numpy as np
import matplotlib.pyplot as plt

obs_data = np.loadtxt("movimiento.dat")
x_obs = obs_data[:,0]
y_obs = obs_data[:,1]

def likelihood(y_obs, y_model):
	return np.exp(0.5*np.sum(y_obs-y_model))

def my_model(x, a, b, c):
	return a*x*x + b*x + c

a_walk = []
b_walk = []
c_walk = []
l_walk = []

a_walk = np.append(a_walk, np.random.random())
b_walk = np.append(b_walk, np.random.random())
c_walk = np.append(c_walk, np.random.random())

y_init = my_model(x_obs, a_walk[0], b_walk[0], c_walk[0])
l_walk = np.append(l_walk, likelihood(y_obs, y_init))

n_iterations = 20000 #this is the number of iterations I want to make
for i in range(n_iterations):
    a_prime = np.random.normal(a_walk[i], 0.1) 
    b_prime = np.random.normal(b_walk[i], 0.1)
    c_prime = np.random.normal(c_walk[i], 0.1)

    y_init = my_model(x_obs, a_walk[i], b_walk[i], c_walk[i])
    y_prime = my_model(x_obs, a_prime, b_prime, c_prime)
    
    l_prime = likelihood(y_obs, y_prime)
    l_init = likelihood(y_obs, y_init)
    
    alpha = l_prime/l_init
    if(alpha>=1.0):
        a_walk  = np.append(a_walk,a_prime)
        b_walk  = np.append(b_walk,b_prime)
        c_walk  = np.append(c_walk,c_prime)
        l_walk = np.append(l_walk, l_prime)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            a_walk = np.append(a_walk,a_prime)
            b_walk = np.append(b_walk,b_prime)
            c_walk = np.append(c_walk,c_prime)
            l_walk = np.append(l_walk, l_prime)
        else:
            a_walk = np.append(a_walk,a_walk[i])
            b_walk = np.append(b_walk,b_walk[i])
            c_walk = np.append(c_walk,c_walk[i])
            l_walk = np.append(l_walk, l_init)

max_likelihood_id = np.argmax(l_walk)
best_a  = a_walk[max_likelihood_id]
best_b  = b_walk[max_likelihood_id]
best_c  = c_walk[max_likelihood_id]
best_y = my_model(x_obs, best_a, best_b, best_c)

plt.scatter(x_obs,y_obs)
plt.plot(x_obs, best_y)
plt.show()
