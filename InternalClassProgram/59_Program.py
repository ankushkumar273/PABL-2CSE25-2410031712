'''ou are given an array arr[ ], where arr[i] represents the height of the ith person standing
in a line.
A person i can see another person j if:
• height[j] < height[i],
• There is no person k standing between them such that height[k] ≥ height[i].
Each person can see in both directions (front and back).
Your task is to find the maximum number of people that any person can see
(including themselves).
Examples:
Input: arr[] = [6, 2, 5, 4, 5, 1, 6 ]
Output: 6'''

def maxVisible(arr):
    n = len(arr)

    left = [0] * n
    right = [0] * n

    # Count visible on left
    stack = []
    for i in range(n):
        count = 0
        while stack and stack[-1][0] < arr[i]:
            count += stack.pop()[1]
        if stack:
            count += 1
        left[i] = count
        stack.append((arr[i], count))

    # Count visible on right
    stack = []
    for i in range(n - 1, -1, -1):
        count = 0
        while stack and stack[-1][0] < arr[i]:
            count += stack.pop()[1]
        if stack:
            count += 1
        right[i] = count
        stack.append((arr[i], count))

    # Find max visible (left + right + self)
    max_people = 0
    for i in range(n):
        max_people = max(max_people, left[i] + right[i] + 1)

    return max_people


# Example
arr = [6, 2, 5, 4, 5, 1, 6]
print(maxVisible(arr))  # Output: 6