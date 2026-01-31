def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    # Swap elements until the two pointers meet
    while left < right:
        # Swap arr[left] and arr[right]
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1


# Example usage
arr = [1, 4, 3, 2, 6, 5]
print("Original array:", arr)

reverse_array(arr)

print("Reversed array:", arr)
