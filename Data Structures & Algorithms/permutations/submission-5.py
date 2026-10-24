class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(stack, nums):
            if not nums:
                res.append(stack.copy())
                
            for i in range(len(nums)):
                stack.append(nums[i])
                backtrack(stack, nums[:i]+nums[i+1:])
                stack.pop()
           
        backtrack([], nums)
        return res
        