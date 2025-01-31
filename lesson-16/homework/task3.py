import numpy as np


# Coefficients matrix (A) and constants vector (b)
A = np.array([[4, 5, 6],
              [3, -1, 1],
              [2, 1, -2]])
b = np.array([7, 4, 5])

# Solve the system
solution = np.linalg.solve(A, b)
print("Solution to the system of equations:", solution)