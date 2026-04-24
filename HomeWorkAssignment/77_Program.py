'''Shortest substring containing all vowels
You are given two strings, s1 and s2, where s1 contains distinct lowercase vowels (a,
e, i, o, u), and s2 contains lowercase English letters. Your task is to find the length of
the shortest contiguous substring within s2 that contains all the vowels present in s1 at
least once, in any order.
Note: If there is no such substring in s2, return -1.
Examples:
Input: s1 = "ae", s2 = "acbaudeq"
Output: 4'''

from collections import Counter

def shortestSubstring(s1, s2):
    need = Counter(s1)
    required = len(need)
    
    window = {}
    formed = 0
    
    left = 0
    min_len = float('inf')
    
    for right in range(len(s2)):
        char = s2[right]
        window[char] = window.get(char, 0) + 1
        
        if char in need and window[char] == need[char]:
            formed += 1
        
        # Try shrinking window
        while formed == required:
            min_len = min(min_len, right - left + 1)
            
            left_char = s2[left]
            window[left_char] -= 1
            
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1
            
            left += 1
    
    return min_len if min_len != float('inf') else -1


# Example
s1 = "ae"
s2 = "acbaudeq"
print(shortestSubstring(s1, s2))  # Output: 4