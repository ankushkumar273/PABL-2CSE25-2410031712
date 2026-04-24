'''Winner of an election
Given a lowercase string array arr[]. Each element in the array represents a vote cast
for a candidate. Return the name of the candidate who received the maximum number
of votes and the count of votes he received. In case of a tie between two or more
candidates, return the lexicographically smallest name.
Note: Return an array of strings, the winning candidate name as the first element and
the vote count as the second element (typecast the count to string).
Examples :
Input: arr[] = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie",
"john", "johnny", "jamie", "johnny", "john"]
Output: ["john", "4"]'''

from collections import Counter

def winner(arr):
    freq = Counter(arr)
    
    max_votes = max(freq.values())
    
    # Get all candidates with max votes
    candidates = [name for name in freq if freq[name] == max_votes]
    
    # Choose lexicographically smallest
    winner_name = min(candidates)
    
    return [winner_name, str(max_votes)]


# Example
arr = ["john", "johnny", "jackie", "johnny", "john", "jackie",
       "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]

print(winner(arr))  # Output: ["john", "4"]