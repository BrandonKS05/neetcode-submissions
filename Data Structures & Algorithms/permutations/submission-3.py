class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current, nums):
            if not nums:
                res.append(current[:])
            for i in range(len(nums)):
                current.append(nums[i])
                backtrack(current, nums[:i] + nums[i+1:])
                current.pop()
        backtrack([], nums)
        return res
        