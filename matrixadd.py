import numpy as np

# Define two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Compute the dot product
dot_product = np.dot(matrix1, matrix2)
# or using the @ operator: dot_product = matrix1 @ matrix2

print(dot_product)

