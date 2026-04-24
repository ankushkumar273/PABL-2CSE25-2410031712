'''Count Unique Vowel Strings
You are given a lowercase string s, determine the total number of distinct strings that
can be formed using the following rules:
• Identify all unique vowels (a, e, i, o, u) present in the string.
• For each distinct vowel, choose exactly one of its occurrences from s. If a
vowel appears multiple times, each occurrence represents a unique selection
choice.
• Generate all possible permutations of the selected vowels. Each unique
arrangement counts as a distinct string.
Return the total number of such distinct strings.
Examples:
Input: s = "aeiou"
Output: 120'''

from math import factorial
from collections import Counter

def countVowelStrings(s):
    vowels = set('aeiou')
    freq = Counter(s)
    
    selected = []
    
    for v in vowels:
        if v in freq:
            selected.append(freq[v])
    
    if not selected:
        return 0
    
    # Product of frequencies
    product = 1
    for x in selected:
        product *= x
    
    k = len(selected)
    
    return product * factorial(k)


# Example
s = "aeiou"
print(countVowelStrings(s))  # Output: 120