
def multiply_matrices(mat1, mat2):

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




