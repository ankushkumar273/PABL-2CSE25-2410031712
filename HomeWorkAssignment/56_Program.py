'''You are given an integer array arr[ ]. For every element in the array, your task is to
determine its Previous Greater Element (PGE).
The Previous Greater Element (PGE) of an element x is the first element that appears to
the left of x in the array and is strictly greater than x.
Note: If no such element exists, assign -1 as the PGE for that position.
Examples:
Input: arr[] = [10, 4, 2, 20, 40, 12, 30]
Output: [-1, 10, 4, -1, -1, 40, 40]'''

def previousGreaterElements(arr):
    stack = []
    result = []

    for num in arr:
        # Remove elements <= current
        while stack and stack[-1] <= num:
            stack.pop()

        # If stack empty → no greater element
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        # Push current element
        stack.append(num)

    return result


# Example
arr = [10, 4, 2, 20, 40, 12, 30]
print(previousGreaterElements(arr))
# Output: [-1, 10, 4, -1, -1, 40, 40]