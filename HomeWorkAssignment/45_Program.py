'''Given an integer array nums of unique elements, return all possible subsets (the power
set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]'''

def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])  # add current subset
        
        for i in range(start, len(nums)):
            path.append(nums[i])          # choose
            backtrack(i + 1, path)       # explore
            path.pop()                   # un-choose (backtrack)

    backtrack(0, [])
    return result

# Example
nums = [1, 2, 3]
print(subsets(nums))