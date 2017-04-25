import numpy as np

vector = np.array([0,4,6])

matriz = np.matrix([[1,3,5],[3,4,6],[5,6,4]])

vector1 = np.array([4,7,8])

A = np.matrix([[2, -2], [5,1]])
b = np.array([2,3])

print matriz, vector, vector1, 3*vector, np.dot(vector, vector1), np.linalg.det(matriz), np.dot(matriz, vector), np.linalg.norm(vector)

print A, b, np.linalg.solve(A,b) 
print np.linalg.inv(A)
