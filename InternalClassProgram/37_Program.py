
'''Given an array of distinct integers candidates and a target integer target, return a list of
all unique combinations of candidates where the chosen numbers sum to target. You
may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is
different.
The test cases are generated such that the number of unique combinations that sum up
to target is less than 150 combinations for the given input.'''

def combinationSum(candidates, target):
    result = []

    def backtrack(start, current, total):
        # ✅ if sum matches target
        if total == target:
            result.append(current[:])
            return
        
        # ❌ if sum exceeds
        if total > target:
            return
        
        # try all options
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])  # reuse same element
            current.pop()  # backtrack

    backtrack(0, [], 0)
    return result


# 👇 Run example
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    
    print("Output:", combinationSum(candidates, target))