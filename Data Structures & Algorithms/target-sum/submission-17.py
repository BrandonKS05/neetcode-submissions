from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def bt(i, total):
            if i >= len(nums): 
                return 1 if total == target else 0
                
            return bt(i + 1, total + nums[i]) + bt(i + 1, total - nums[i])
        return bt(0, 0)
        

       