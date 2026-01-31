def find_min_max(arr):
    # Assume first element is both min and max initially
    minimum = arr[0]
    maximum = arr[0]

    # Traverse the array
    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum


# Example usage
arr = [1, 4, 3, 5, 8, 6]
print("Array:", arr)

min_val, max_val = find_min_max(arr)
print("Minimum:", min_val)
print("Maximum:", max_val)
