class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(start, cur_sum, stack):
            if cur_sum == target:
                res.append(stack.copy())
                return
            if cur_sum > target:
                return
        
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                stack.append(candidates[i])
                backtrack(i + 1, cur_sum + candidates[i], stack)
                stack.pop()
                   
        backtrack(0, 0, [])
        return res


        