'''Lexicographically Largest String After K Deletions
Given a string s consisting of lowercase English letters and an integer k, your task is to
remove exactly k characters from the string. The resulting string must be the largest
possible in lexicographical order, while maintain the relative order of the remaining
characters.
Examples:
Input: s = "ritz", k = 2
Output: tz '''

def largestStringAfterKDeletions(s, k):
    stack = []
    
    for ch in s:
        while stack and k > 0 and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)
    
    # If k still remains, remove from end
    while k > 0:
        stack.pop()
        k -= 1
    
    return "".join(stack)


# Example
s = "ritz"
k = 2
print(largestStringAfterKDeletions(s, k))  # Output: "tz"