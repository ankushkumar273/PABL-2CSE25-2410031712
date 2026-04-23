import bisect

def rowWithMax1s(arr):
    n = len(arr)
    m = len(arr[0])

    max_ones = 0
    row_index = -1

    for i in range(n):
        # Find first occurrence of 1
        first_one = bisect.bisect_left(arr[i], 1)

        if first_one < m:  # 1 exists in the row
            ones_count = m - first_one

            if ones_count > max_ones:
                max_ones = ones_count
                row_index = i

    return row_index