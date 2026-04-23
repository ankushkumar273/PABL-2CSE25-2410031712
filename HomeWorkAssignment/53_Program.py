'''Given an array arr[], find the minimum number of operations required to make the
sum of its elements less than or equal to half of the original sum. In one operation, you
may replace any element with half of its value (with floating-point precision).
Examples:
Input: arr[] = [8, 6, 2]
Output: 3
'''

import heapq

def minOperations(arr):
    total_sum = sum(arr)
    target = total_sum / 2

    # Max heap (store negatives because Python has min-heap)
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)

    current_sum = total_sum
    operations = 0

    while current_sum > target:
        # Get largest element
        largest = -heapq.heappop(max_heap)
        
        # Reduce it to half
        half = largest / 2
        
        # Update sum
        current_sum -= half
        
        # Push the new value back
        heapq.heappush(max_heap, -half)
        
        operations += 1

    return operations


# Example
arr = [8, 6, 2]
print(minOperations(arr))  # Output: 3