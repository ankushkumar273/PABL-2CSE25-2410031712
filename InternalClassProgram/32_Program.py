from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, remaining):
            # Base case: if remaining is 0, we found a valid combination
            if remaining == 0:
                result.append(list(current))
                return
            
            # If remaining is negative, stop exploring this path
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                # Reuse the same element, so pass i (not i+1)
                backtrack(i, current, remaining - candidates[i])
                current.pop()  # backtrack

        backtrack(0, [], target)
        return result