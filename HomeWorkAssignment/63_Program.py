'''Given a sorted array arr[] containing distinct non negative integers that has been
rotated at some unknown pivot, and a value x. Your task is to count the number of
elements in the array that are less than or equal to x.
Examples:
Input: arr[] = [4, 5, 8, 1, 3], x = 6
Output: 4
'''

def countLessEqual(arr, x):
    n = len(arr)

    # Step 1: Find pivot (smallest element index)
    def findPivot():
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        return left

    pivot = findPivot()

    # Step 2: Binary search to count ≤ x
    def countLE(left, right):
        count = 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                count = mid - left + 1
                left = mid + 1
            else:
                right = mid - 1
        return count

    # Count in both parts
    count = 0
    count += countLE(0, pivot - 1)
    count += countLE(pivot, n - 1)

    return count


# Example
arr = [4, 5, 8, 1, 3]
x = 6
print(countLessEqual(arr, x))  # Output: 4