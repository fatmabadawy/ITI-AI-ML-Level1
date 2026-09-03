# Part-3
import numpy as np
# 1- Create two vectors a = [1, 2, 3] and b = [4, 5, 6]. Compute element-wise addition,
# subtraction, and dot product.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Dot Product:", np.dot(a, b))


# 2- Multiply a 2x3 matrix [[1, 2, 3], [4, 5, 6]] with a 3x2 matrix [[7, 8], [9, 10], [11, 12]].

a=np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8],[9, 10], [11, 12]])

result = np.dot(a, b)

print(result)

# 3- Transpose a matrix [[1, 2], [3, 4], [5, 6]].

a=np.array([[1, 2], [3, 4], [5, 6]])

print(np.transpose(a))

# 4- Create a 4x4 identity matrix.

a = np.eye(4)

print(a)

# 5- Compute the inverse of [[4, 7], [2, 6]].

A = np.array([[4, 7],
              [2, 6]])

inverse = np.linalg.inv(A)

print(inverse)


# 6- Solve Ax = b where A = [[3, 1], [1, 2]] and b = [9, 8].

a = np.array([[3, 1],[1, 2]])

b = np.array([9, 8])

x = np.linalg.solve(a, b)

print(x)

# 7- Find eigenvalues and eigenvectors of [[2, -1], [-1, 2]].

A = np.array([[2, -1],
              [-1, 2]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)

# 8- Compute the determinant of [[1, 2], [3, 4]].

a = np.array([[1, 2],[3, 4]])

det = np.linalg.det(a)

print(round(det))