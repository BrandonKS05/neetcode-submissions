class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = {}
        def backtrack(i, total):
            if (i, total) in m:
                return m[(i, total)]

            if i >= len(nums): 
                return 1 if total == target else 0
                

            m[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            
            return m[(i, total)]
       
        return backtrack(0, 0)
        

       