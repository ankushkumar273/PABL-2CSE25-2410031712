'''You are given an m x n integer matrix matrix with the following two properties:
• Each row is sorted in non-decreasing order.
• The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity'''

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        
        # convert to 2D index
        row = mid // cols
        col = mid % cols
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# 👇 Run example
if __name__ == "__main__":
    matrix = [[1,3,5,7],
              [10,11,16,20],
              [23,30,34,60]]
    
    target = 3
    print("Output:", searchMatrix(matrix, target))