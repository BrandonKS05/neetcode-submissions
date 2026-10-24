class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(current, stack, total):
            if total == target:
                res.append(stack[:])
                return 
            if total > target:
                return

            for i in range(current, len(candidates)):
                if i > current and candidates[i] == candidates[i-1]:
                    continue
                stack.append(candidates[i])
                backtrack(i + 1, stack, total + candidates[i])
                stack.pop()
        backtrack(0, [], 0)
        return res