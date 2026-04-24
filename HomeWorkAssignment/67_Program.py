'''Score of Parentheses String
Given a string s consisting of balanced parentheses, calculate the score of the string
based on the following rules:
• "()" has a score of 1.
• "AB" has a score of A + B, where A and B are balanced parentheses strings.
• "(A)" has a score of 2 × score(A), where A is a balanced parentheses string.
Note: Test cases are generated such that the score will fit within a 32-bit integer.
Examples:
Input: s = "()()"
Output: 2


'''

def scoreOfParentheses(s):
    score = 0
    depth = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            depth += 1
        else:
            depth -= 1
            if s[i-1] == '(':
                score += 2 ** depth
                
    return score


# Example
s = "()()"
print(scoreOfParentheses(s))  # Output: 2