'''Given a collection of candidate numbers (candidates) and a target number (target), find
all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''

def combinationSum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, current, total):
        # ✅ found valid combination
        if total == target:
            result.append(current[:])
            return
        
        # ❌ exceeded target
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            # 🚫 skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            current.append(candidates[i])
            backtrack(i + 1, current, total + candidates[i])  # move forward
            current.pop()

    backtrack(0, [], 0)
    return result


# 👇 Run example
if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    
    print("Output:", combinationSum2(candidates, target))