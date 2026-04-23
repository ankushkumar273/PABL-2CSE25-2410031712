'''Given a integer matrix (or 2D array) a[][] of dimensions n * m. Also, given another 2-
D array query[][] of dimensions q * 4.
For each index 0 < i < query.length, find the sum of all the elements of the rectangular
matrix whose top left corner is (query[i][0], query[i][1]) and bottom right corner is
(query[i][2], query[i][3]).
Example -
Input:
n = 3, m = 3, q = 2
a[][] = [
 [ 1, 2, 3],
 [ 4, 5, 6],
 [ 7, 8, 9]
 ]
query[][] = [
 [0, 0, 2, 2]
 [1, 0, 2, 1]
 ]
Output:
45
24
'''

def rangeSumQuery(matrix, queries):
    n = len(matrix)
    m = len(matrix[0])

    # Step 1: Build prefix sum matrix
    prefix = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            prefix[i][j] = matrix[i][j]

            if i > 0:
                prefix[i][j] += prefix[i - 1][j]
            if j > 0:
                prefix[i][j] += prefix[i][j - 1]
            if i > 0 and j > 0:
                prefix[i][j] -= prefix[i - 1][j - 1]

    # Step 2: Process queries
    result = []
    for r1, c1, r2, c2 in queries:
        total = prefix[r2][c2]

        if r1 > 0:
            total -= prefix[r1 - 1][c2]
        if c1 > 0:
            total -= prefix[r2][c1 - 1]
        if r1 > 0 and c1 > 0:
            total += prefix[r1 - 1][c1 - 1]

        result.append(total)

    return result


# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

queries = [
    [0, 0, 2, 2],
    [1, 0, 2, 1]
]

print(rangeSumQuery(matrix, queries))  # Output: [45, 24]