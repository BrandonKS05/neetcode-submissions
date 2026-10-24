class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            for j in range(n+1,len(nums)):
                if nums[n]+nums[j] == target:
                    return [n,j]
                    

        