'''Given two integers n and k, the task is to find all valid combinations of k numbers that
adds up to n based on the following conditions:
• Only numbers from the range [1, 9] used.
• Each number can only be used at most once.
Note: You can return the combinations in any order, the driver code will print them in
sorted order.
Examples:
Input: n = 9, k = 3
Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]'''

def combinationSum3(k, n):
    result = []

    def backtrack(start, path, target):
        # If valid combination found
        if len(path) == k and target == 0:
            result.append(path[:])
            return
        
        # Stop if invalid
        if len(path) > k or target < 0:
            return

        for i in range(start, 10):  # numbers 1 to 9
            path.append(i)
            backtrack(i + 1, path, target - i)
            path.pop()  # backtrack

    backtrack(1, [], n)
    return result


# Example
n = 9
k = 3
print(combinationSum3(k, n))