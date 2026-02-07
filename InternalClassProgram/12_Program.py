def get_min_diff(arr, k):
    n = len(arr)
    if n == 1:
        return 0

    arr.sort()

    # Initial difference
    ans = arr[-1] - arr[0]

    # Smallest and largest after first modification
    smallest = arr[0] + k
    largest = arr[-1] - k

    for i in range(1, n):
        min_height = min(smallest, arr[i] - k)
        max_height = max(largest, arr[i - 1] + k)

        if min_height < 0:
            continue

        ans = min(ans, max_height - min_height)

    return ans


# Example 1
arr = [1, 5, 8, 10]
k = 2
print(get_min_diff(arr, k))  # Output: 5

# Example 2
arr = [3, 9, 12, 16, 20]
k = 3
print(get_min_diff(arr, k))  # Output: 11
