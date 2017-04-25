import numpy as np

x = [0, 0, 2]
y = [1, 3, 6]
A = np.zeros((3,3))
for i in range(3):
	A[i] = np.array([1, x[i], x[i]**2])
sol = np.linalg.solve(A, y)
print sol
