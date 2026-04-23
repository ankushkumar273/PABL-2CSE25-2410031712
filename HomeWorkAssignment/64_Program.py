'''You will be given a vector of integers of size n containing the elements. Your task is to
find the sum of all the integers present in the array.As the sum can be large you have to
return a value in long long data type.
Example 1:
Input:
n=7
input= {6,2,5,4,5,1,6}
Output : 29
'''

def arraySum(arr):
    total = 0
    for num in arr:
        total += num
    return total


# Example
arr = [6, 2, 5, 4, 5, 1, 6]
print(arraySum(arr))  # Output: 29