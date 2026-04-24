'''Difference Check
Given an array arr[] of time strings in 24-hour clock format "HH:MM:SS", return
the minimum difference in seconds between any two time strings in the arr[].
The clock wraps around at midnight, so the time difference between "23:59:59" and
"00:00:00" is 1 second.
Examples:
Input: arr[] = ["12:30:15", "12:30:45"]
Output: 30
'''

def min_time_difference(arr):
    times = []
    
    # Convert to seconds
    for t in arr:
        h, m, s = map(int, t.split(":"))
        total = h * 3600 + m * 60 + s
        times.append(total)
    
    # Sort times
    times.sort()
    
    # Initialize result
    min_diff = float('inf')
    
    # Check adjacent differences
    for i in range(1, len(times)):
        min_diff = min(min_diff, times[i] - times[i-1])
    
    # Check circular difference (midnight wrap)
    wrap_diff = 86400 - (times[-1] - times[0])
    min_diff = min(min_diff, wrap_diff)
    
    return min_diff


# Example
arr = ["12:30:15", "12:30:45"]
print(min_time_difference(arr))  # Output: 30