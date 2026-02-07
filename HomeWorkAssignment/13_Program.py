def min_jumps(arr):
    n = len(arr)

    # If array has 1 or no element
    if n <= 1:
        return 0

    # If first element is 0, we can't move
    if arr[0] == 0:
        return -1

    jumps = 1
    max_reach = arr[0]
    steps = arr[0]

    for i in range(1, n):
        # If we've reached the end
        if i == n - 1:
            return jumps

        max_reach = max(max_reach, i + arr[i])
        steps -= 1

        # Need to make another jump
        if steps == 0:
            jumps += 1

            # If current position is beyond max reach
            if i >= max_reach:
                return -1

            steps = max_reach - i

    return -1


# Example
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(min_jumps(arr))
