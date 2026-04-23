'''You are given an array arr[] of size n , where arr[i] denotes the range of working hours
a person at position i can cover.
• If arr[i] ≠ -1, the person at index i can work and cover the time interval [i -
arr[i], i + arr[i]].
• If arr[i] = -1, the person is unavailable and cannot cover any time.
The task is to find the minimum number of people required to cover the entire working
day from 0 to n - 1. If it is not possible to fully cover the day, return -1.
Examples:
Input: arr[] = [1, 2, 1, 0]
Output: 1
Explanation: The person at index 1 can cover the interval [-1, 3]. After adjusting to
valid bounds, this becomes [0, 3], which fully covers the entire working day 0 to n -1.
Therefore, only 1 person is required to cover the whole day.
Input: arr[] = [2, 3, 4, -1, 2, 0, 0, -1, 0]
Output: -1
'''

def minPeople(arr):
    n = len(arr)
    intervals = []

    # Step 1: Build intervals
    for i in range(n):
        if arr[i] != -1:
            left = max(0, i - arr[i])
            right = min(n - 1, i + arr[i])
            intervals.append((left, right))

    # Step 2: Sort intervals
    intervals.sort()

    count = 0
    i = 0
    curr_end = 0
    farthest = 0

    # Step 3: Greedy covering
    while curr_end < n:
        while i < len(intervals) and intervals[i][0] <= curr_end:
            farthest = max(farthest, intervals[i][1])
            i += 1

        # If we can't extend further → impossible
        if farthest == curr_end:
            return -1

        count += 1
        curr_end = farthest + 1

    return count


# Examples
print(minPeople([1, 2, 1, 0]))        # Output: 1
print(minPeople([2, 3, 4, -1, 2, 0, 0, -1, 0]))  # Output: -1