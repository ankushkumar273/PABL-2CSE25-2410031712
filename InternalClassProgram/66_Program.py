'''Min Add to Make Parentheses Valid
You are given a string s consisting only of the characters '(' and ')'. Your task is to
determine the minimum number of parentheses (either '(' or ')') that must be inserted at
any positions to make the string s a valid parentheses string.
A parentheses string is considered valid if:
1. Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
2. Every closing parenthesis ')' has a corresponding opening parenthesis '('.
3. Parentheses are properly nested.
Examples:
Input: s = "(()("
Output: 2
'''

def minAddToMakeValid(s):
    balance = 0
    additions = 0

    for ch in s:
        if ch == '(':
            balance += 1
        else:  # ')'
            if balance > 0:
                balance -= 1
            else:
                additions += 1

    return additions + balance


# Example
s = "(()("
print(minAddToMakeValid(s))  # Output: 2