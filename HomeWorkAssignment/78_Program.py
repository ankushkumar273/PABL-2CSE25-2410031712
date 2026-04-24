'''Balancing Consonants and Vowels Ratio
You are given an array of strings arr[], where each arr[i] consists of lowercase english
alphabets. You need to find the number of balanced strings in arr[] which can be
formed by concatinating one or more contiguous strings of arr[].
A balanced string contains the equal number of vowels and consonants.Examples:
Input: arr[] = ["aeio", "aa", "bc", "ot", "cdbd"]
Output: 4'''


def is_vowel(ch):
    return ch in "aeiou"

def countBalanced(arr):
    values = []
    
    # Step 1: Convert each string
    for word in arr:
        v = sum(1 for ch in word if is_vowel(ch))
        c = len(word) - v
        values.append(v - c)
    
    # Step 2: Count subarrays with sum = 0
    prefix_sum = 0
    freq = {0: 1}
    count = 0
    
    for val in values:
        prefix_sum += val
        
        if prefix_sum in freq:
            count += freq[prefix_sum]
        
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    
    return count


# Example
arr = ["aeio", "aa", "bc", "ot", "cdbd"]
print(countBalanced(arr))  # Output: 4