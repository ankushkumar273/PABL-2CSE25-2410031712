'''Given an array arr[] of integers and an integer k, select k elements from the array such
that the minimum absolute difference between any two of the selected elements
is maximized. Return this maximum possible minimum difference.
Examples:
Input: arr[] = [2, 6, 2, 5], k = 3
Output: 1
'''

def maxMinDiff(arr, k):
    arr.sort()

    # Check if we can pick k elements with at least 'mid' difference
    def canPick(mid):
        count = 1
        last = arr[0]

        for i in range(1, len(arr)):
            if arr[i] - last >= mid:
                count += 1
                last = arr[i]
                if count == k:
                    return True
        return False

    left, right = 0, arr[-1] - arr[0]
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if canPick(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


# Example
arr = [2, 6, 2, 5]
k = 3
print(maxMinDiff(arr, k))  # Output: 1