def two_sum(nums, target):
    seen = {}  # dictionary to store number and its index

    for i in range(len(nums)):
        needed = target - nums[i]   # value we need to find

        if needed in seen:
            return [seen[needed], i]  # found the pair

        seen[nums[i]] = i   # store current number with index

# Example
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print("Indices:", result)
