def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Phase 1: Detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# Examples
print(find_duplicate([1, 3, 4, 2, 2]))   # Output: 2
print(find_duplicate([3, 1, 3, 4, 2]))   # Output: 3
print(find_duplicate([3, 3, 3, 3, 3]))   # Output: 3
