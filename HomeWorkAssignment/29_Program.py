import bisect

def findMedian(mat):
    n = len(mat)
    m = len(mat[0])

    # Minimum and maximum elements in the matrix
    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)

    desired = (n * m) // 2

    while low <= high:
        mid = (low + high) // 2

        # Count elements less than or equal to mid
        count = 0
        for row in mat:
            count += bisect.bisect_right(row, mid)

        if count <= desired:
            low = mid + 1
        else:
            high = mid - 1

    return low