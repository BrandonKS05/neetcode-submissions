class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, total_sum, stack):
            if total_sum == target:
                res.append(stack.copy())
            if total_sum > target:
                return
    
            for i in range(start, len(nums)):
                stack.append(nums[i])
                backtrack(i, total_sum + nums[i], stack)
                stack.pop()
            return 
        backtrack(0, 0, [])
        return res

        