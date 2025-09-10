import numpy as np

def matrix_input():
    rows = int(input("Enter rows: "))
    cols = int(input("Enter cols: "))
    mat = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        mat.append(row)
    return np.array(mat)

print("Enter Matrix A:")
A = matrix_input()
print("Enter Matrix B:")
B = matrix_input()

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

print("\nAddition:\n", A + B)
print("Subtraction:\n", A - B)
print("Multiplication:\n", A @ B)
print("Transpose of A:\n", A.T)
print("Determinant of A:\n", np.linalg.det(A))
