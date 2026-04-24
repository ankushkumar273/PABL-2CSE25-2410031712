'''Count pairs of strings with one mismatch
Given an array arr[] of strings of equal length, where each string consists of lowercase
English letters, find the total number of pairs of strings that differ in exactly one
character position.
Note: Two strings differ in exactly one position if they have the same length and differ
in exactly one index that is, all characters except one are the same.
Examples :
Input: arr[] = ["abc", "abd", "bbd"]
Output: 2'''

def countPairs(arr):
    n = len(arr)
    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            diff = 0
            
            for k in range(len(arr[i])):
                if arr[i][k] != arr[j][k]:
                    diff += 1
                    if diff > 1:
                        break
            
            if diff == 1:
                count += 1
                
    return count


# Example
arr = ["abc", "abd", "bbd"]
print(countPairs(arr))  # Output: 2