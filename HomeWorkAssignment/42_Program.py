'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column
to 0's'''

def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

    # mark zeros in first row & column
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # set elements to zero based on marks
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # handle first row
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # handle first column
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0


# 👇 Run example
if __name__ == "__main__":
    matrix = [[1,1,1],
              [1,0,1],
              [1,1,1]]
    
    setZeroes(matrix)
    print("Output:", matrix)