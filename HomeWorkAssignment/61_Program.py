'''Given an array arr[] of size n, your task is to divide the array in two subsets such that
the absolute difference between the sum of elements in the two subsets is equal
to zero (i.e., both subsets have the same sum).
• If n is even, both subsets must contain exactly n/2 elements.
• If n is odd, one subset must contain (n-1)/2 elements and the other subset must
contain (n+1)/2 elements.
Note : If multiple answers exist, you may return any of them. The driver code will
check and print true if your partition is valid, otherwise false.
It is guaranteed that there will always be atleast one valid partition.
Examples:
Input: arr[] = [1, 2, 3, 4]
Output: [[1, 4], [2, 3]]
'''

def partitionArray(arr):
    n = len(arr)
    total = sum(arr)

    target = total // 2
    k = n // 2  # size of first subset

    result = []

    def backtrack(start, path, curr_sum):
        # If valid subset found
        if len(path) == k and curr_sum == target:
            result.append(path[:])
            return True
        
        if len(path) > k or curr_sum > target:
            return False

        for i in range(start, n):
            path.append(arr[i])
            if backtrack(i + 1, path, curr_sum + arr[i]):
                return True
            path.pop()

        return False

    backtrack(0, [], 0)

    subset1 = result[0]
    subset2 = arr[:]

    # Remove elements of subset1 from subset2
    for x in subset1:
        subset2.remove(x)

    return [subset1, subset2]


# Example
arr = [1, 2, 3, 4]
print(partitionArray(arr))