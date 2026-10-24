class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(start, stack, total):
            if total == target:
                res.append(stack[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                stack.append(candidates[i])
                backtrack(i + 1, stack, total + candidates[i])
                stack.pop()
          
        backtrack(0,[], 0)
        return res
 
     

     

     
         


            