def combinationSum(candidates, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result

candidates = [2, 3, 6, 7]
target = 7

result = combinationSum(candidates, target)
print("Combinations:", result)
