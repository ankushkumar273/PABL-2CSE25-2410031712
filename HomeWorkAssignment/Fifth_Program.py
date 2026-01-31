def find_largest(arr):
    # Assume the first element is the largest
    largest = arr[0]

    # Traverse the array
    for num in arr:
        if num > largest:
            largest = num

    return largest


# Example usage
arr = [1, 8, 7, 56, 90]

print("Array:", arr)
result = find_largest(arr)
print("Largest element:", result)
