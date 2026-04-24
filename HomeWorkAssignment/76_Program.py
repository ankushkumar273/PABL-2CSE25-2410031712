'''Count Even Letters
You are given a string s consisting of lowercase english letters. Your task is to count
how many distinct characters appear an even number of times in the string.
Examples:
Input: s = "abacaba"
Output: 2'''

from collections import Counter

def countEvenLetters(s):
    freq = Counter(s)
    
    count = 0
    for ch in freq:
        if freq[ch] % 2 == 0:
            count += 1
            
    return count


# Example
s = "abacaba"
print(countEvenLetters(s))  # Output: 2