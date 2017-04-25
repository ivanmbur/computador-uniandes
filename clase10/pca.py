import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("room-temperature-processed.csv")

cov =  np.cov(data.T)

values, vectors = np.linalg.eig(cov)

rotated_data = np.dot(vectors.T, data.T)

plt.scatter(rotated_data[0,:], rotated_data[1,:])
plt.show()
