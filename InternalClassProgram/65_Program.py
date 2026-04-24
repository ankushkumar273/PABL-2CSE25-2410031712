'''You are given two binary strings s1 and s2 of equal length, and the task is to find
the minimum number of swaps required to make them identical. The only allowed
operation is swapping characters between the two strings (i.e., you can
swap s1[i] with s2[j], but not within the same string). If it is impossible to make the two
strings equal through such swaps, return -1.
Examples:
Input: s1 = "1100", s2 = "1111"
Output: 1
'''

def min_swaps(s1, s2):
    x = y = 0
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == '1':
                x += 1
            else:
                y += 1

    # If mismatches are odd → impossible
    if (x + y) % 2 != 0:
        return -1

    return (x + y) // 2


# Example
s1 = "1100"
s2 = "1111"
print(min_swaps(s1, s2))  # Output: 1