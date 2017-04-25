import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data_rand.txt")
plt.plot(data[:,0], data[:,1])
plt.savefig("bono.pdf")
plt.show()
