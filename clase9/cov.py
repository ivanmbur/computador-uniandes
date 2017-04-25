import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data_B.txt")

size = len(data[:,0])

cov = np.zeros((2,2))

average = np.array([np.mean(dat) for dat in data])

for i in range(0,2):
	for j in range(0,2):
		for k in range(0,size):
			cov[i][j] += (data[k][i] - average[i]) * (data[k][j] - average[j]) / (size - 1)

values, vectors = np.linalg.eig(cov)

pos = values.argsort()

values = values[pos][::-1]
vectors = vectors[pos][::-1]


plt.plot(data[:,0], data[:,1], "o", ms = 1)
x = np.linspace(-7, 7, 100)
plt.plot(x, x*vectors[1,0]/vectors[0,0])
plt.plot(x, x*vectors[1,1]/vectors[0,1])
plt.show() 
