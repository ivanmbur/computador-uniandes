import numpy as np

def gauss_jordan(A, b):

	n = len(A)
	B = np.zeros((n, n+1))
	
	#Extender la matriz
	
	for i in range(0,n):
		B[i] = np.append(A[i], [b[i]])

	#Reduccion

	for j in range(0,n):
		I = 0
		testigo = False
		while testigo == False:
			if (B[I][j] != 0):
				testigo = True
			else:
				I += 1
	a = B[I][j]
	B[I] = B[I]/a
	for i in range(0,n):
		if i != I:
			B[i] = B[i] - B[i][j]*B[I]

	return B

A = np.array([[4, 5], [1,2]])
b = np.array([32, 11])

print gauss_jordan(A, b) 
