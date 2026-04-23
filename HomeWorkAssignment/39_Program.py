'''You are given a 0-indexed array of integers nums of length n. You are initially
positioned at index 0.
Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at index i, you can jump to any index (i + j) where:
• 0 <= j <= nums[i] and
• i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated
such that you can reach index n - 1.
Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
'''
def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        # update farthest we can reach
        farthest = max(farthest, i + nums[i])

        # if we reach end of current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps


# 👇 Run example
if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print("Output:", jump(nums))