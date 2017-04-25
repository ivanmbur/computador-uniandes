import numpy as np
import matplotlib.pyplot as plt


n = 100000
bins = np.arange(1, 11)
x = np.random.random(n)
plt.hist(x, bins = 10, normed = True)
plt.savefig("gauss.png")
