# Function to add two matrices
def add_matrices(mat1, mat2):
    # Checking if the matrices have the same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions for addition"
    
    # Initialize an empty result matrix with the same dimensions
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result


matrix1 = [
    [1, 2, 3,],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Calling the add_matrices function
resultMatrix = add_matrices(matrix1, matrix2)

# Displaying the results
if isinstance(resultMatrix, str):
    print(resultMatrix)
else:
    print("Sum of matrices: ")
    for row in resultMatrix:
        print(row)


