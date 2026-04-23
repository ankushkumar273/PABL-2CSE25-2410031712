'''Given an array of integers nums sorted in non-decreasing order, find the starting and
ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]. code in python  '''

def searchRange(nums, target):
    
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                first = mid
                right = mid - 1  # move left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return first

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                last = mid
                left = mid + 1  # move right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return last

    return [findFirst(nums, target), findLast(nums, target)]


# Example
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]