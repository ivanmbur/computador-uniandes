import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.array([[float(T) for T in line.rstrip("\r\n").split(",")[1:]] for line in open("room-temperature.csv", "r").readlines()[1:]])
mediciones = len(temperaturas)
esquinas = len(temperaturas[0])

fig, ax = plt.subplots(esquinas, sharex = True)
ax[esquinas - 1].set_xlabel("Tiempo")
for i in range(0, esquinas):
	ax[i].plot(np.arange(mediciones), temperaturas[:,i], label = "Esquina %d" % (i+1))
	ax[i].set_ylabel("temperatura")
	ax[i].legend(loc = 1)
fig.savefig("room.pdf")


for i in range(0, esquinas):
	temperaturas[:,i] = (temperaturas[:,i] - np.mean(temperaturas[:,i]))/np.std(temperaturas[:,i])

cov = np.cov(temperaturas.T)
print "La matriz de covarianza es:\n", cov 

valores, vectores = np.linalg.eig(cov)
#Los calores ya estan en orden
print "La primera componente principal es", vectores[0], "con valor", valores[0]
print "La segunda componente principal es", vectores[1], "con valor", valores[1]

print "La primera componente principal explica el", valores[0]*100/np.sum(valores), "% de la varianza"
print "La segunda componente principal explica el", valores[1]*100/np.sum(valores), "% de la varianza"

fig, ax = plt.subplots()
ax.scatter(temperaturas[:,0], temperaturas[:,1])
X = np.linspace(0, np.amax(temperaturas[:,0]), 100)
ax.plot(X, X*vectores[0,1]/vectores[0,0]) 
ax.plot(X, X*vectores[1,1]/vectores[1,0])
fig.savefig("pca_fr_fl.pdf")
fig, ax = plt.subplots()
ax.scatter(temperaturas[:,0], temperaturas[:,2])
X = np.linspace(0, np.amax(temperaturas[:,0]), 100)
ax.plot(X, X*vectores[0,2]/vectores[0,0]) 
ax.plot(X, X*vectores[1,2]/vectores[1,0])
fig.savefig("pca_bl_fl.pdf")
