import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
from scipy.stats import norm

n = []
for i in range(1000):
	n.append(np.random.exponential(10))

sigma, media = expon.fit(n)
x = np.linspace(0, 50, 100)
y = expon.pdf(x, scale = media)

f, figura1 = plt.subplots(1, 1)
figura1.hist(n, bins = 50, normed = True)
figura1.plot(x, y)
f.savefig("histograma1.png")
