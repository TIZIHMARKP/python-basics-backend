# Function to transpose a matrix
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    # Creating an empty matrix to store the transposed data
    result = [[0 for _ in range(rows)] for _ in range(cols) ]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result

# Input matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Transposing the matrix
transpose_matrix = transpose_matrix(matrix)

# Printing the transposed matrix
for row in transpose_matrix:
    print(row)

