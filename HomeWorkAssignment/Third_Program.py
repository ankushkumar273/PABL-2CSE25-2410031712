def kth_smallest(arr, k):
    # Sort the array
    arr.sort()

    # k-th smallest element (k-1 index because index starts from 0)
    return arr[k - 1]


# Example usage
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

print("Array:", arr)
print("k =", k)

result = kth_smallest(arr, k)
print("Kth smallest element:", result)
