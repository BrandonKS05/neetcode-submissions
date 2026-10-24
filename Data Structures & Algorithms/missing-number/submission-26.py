class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        x = 0
        for n in range(len(nums)):
            if x != nums[n]:
                return(x)
            x += 1
            if x == len(nums):
                return x