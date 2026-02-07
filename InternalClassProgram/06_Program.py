def rotate_clockwise_by_one(arr):
    if len(arr) == 0:
        return arr  # empty array

    last_element = arr[-1]      # take last element
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]     # shift elements to the right

    arr[0] = last_element       # put last element at first position
    return arr

# Example
arr = [1, 2, 3, 4, 5]
result = rotate_clockwise_by_one(arr)
print("Rotated Array:", result)
