'''Sort by Frequency
Given a string s, the task is to arrange the string according to the frequency of each
character, in ascending order. If two elements have the same frequency, then they are
sorted in lexicographical order.
Examples:
Input: s = "geeksforgeeks"
Output: forggkksseee'''

from collections import Counter

def frequencySort(s):
    freq = Counter(s)
    
    # Sort by frequency, then character
    sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
    
    result = ""
    for ch, count in sorted_chars:
        result += ch * count
        
    return result


# Example
s = "geeksforgeeks"
print(frequencySort(s))  # Output: forggkksseee