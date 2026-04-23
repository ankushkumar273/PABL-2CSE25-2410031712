'''Given a matrix a of size n*m which represents a park, there is some construction work
needs to be done. You are also given q queries each query contains two
numbers R and C, For every query we need to construct a footpath in the Rth row
and Cth column, there is a cost of this construction, after the construction this path will
divide the park into sections, and the cost of the construction is
the sum of minimum value present in all the sections. You are asked to find this cost
for all the queries.
Note: Elements present in queries array are according to 1-based indexing.
Example 1:
Input:
n=3
m=3
a={{1,2,3},{4,5,6},{7,8,9}}  q=1
queries={{2,2}}
Output:
20. code in python'''


def constructionCost(matrix, queries):
    n = len(matrix)
    m = len(matrix[0])
    results = []

    for R, C in queries:
        # Convert to 0-based index
        r, c = R - 1, C - 1

        mins = []

        # Top-left
        if r > 0 and c > 0:
            mins.append(min(matrix[i][j] for i in range(r) for j in range(c)))

        # Top-right
        if r > 0 and c < m - 1:
            mins.append(min(matrix[i][j] for i in range(r) for j in range(c + 1, m)))

        # Bottom-left
        if r < n - 1 and c > 0:
            mins.append(min(matrix[i][j] for i in range(r + 1, n) for j in range(c)))

        # Bottom-right
        if r < n - 1 and c < m - 1:
            mins.append(min(matrix[i][j] for i in range(r + 1, n) for j in range(c + 1, m)))

        results.append(sum(mins))

    return results


# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

queries = [[2, 2]]

print(constructionCost(matrix, queries))  # Output: [20]