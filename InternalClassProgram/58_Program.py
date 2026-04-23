'''You are given an array arr[]. The task is to determine whether the array contains a 132
pattern, i.e., three indices i, j and k such that i < j < k , arr[i] < arr[j] >
arr[k] and arr[i] < arr[k].
Return true if such a triplet exists, otherwise return false.
Examples:
Input: arr[] = [4, 7, 11, 5, 13, 2]
Output: true'''

def find132pattern(arr):
    stack = []
    third = float('-inf')  # represents arr[k]

    # Traverse from right
    for num in reversed(arr):
        # If we find arr[i] < arr[k]
        if num < third:
            return True

        # Update 'third' (arr[k])
        while stack and stack[-1] < num:
            third = stack.pop()

        # Push current element as potential arr[j]
        stack.append(num)

    return False


# Example
arr = [4, 7, 11, 5, 13, 2]
print(find132pattern(arr))  # Output: True