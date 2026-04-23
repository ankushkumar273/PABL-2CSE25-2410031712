'''def previousGreaterElements(arr):
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
# Output: [-1, 10, 4, -1, -1, 40, 40]'''

def previousGreaterElements(arr):
    stack = []   # will store candidates for PGE
    result = []

    for current in arr:
        while stack and stack[-1] <= current:
            stack.pop()

        result.append(stack[-1] if stack else -1)
        stack.append(current)

    return result
arr = [10, 4, 2, 20, 40, 12, 30]
print(previousGreaterElements(arr))