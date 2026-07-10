# ========== This program multiplies two matrices and prints the result ===========

#  Function to multiply two matrices
def multiply_matrices(mat1, mat2):

    # Checking if the matrices can be multiplied by determining the dimensions of the matrices
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])

    if cols1 != rows2:
        return "Matrix multiplication is not possible. The number of columns in the first matrix must be equal to the number of rows in the second matrix."
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]


resultMatrix = multiply_matrices(matrix1, matrix2)

if isinstance(resultMatrix, str):
    print(resultMatrix)
else:
    print("Result of matrix multiplication")
    for row in resultMatrix:
        print(row)


