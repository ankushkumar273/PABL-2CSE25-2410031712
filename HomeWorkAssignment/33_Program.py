from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to handle duplicates
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicate elements
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()  # backtrack

        backtrack(0, [], target)
        return result