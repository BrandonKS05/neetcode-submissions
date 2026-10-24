from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        # 1, 2, 4,  6
        for i,num in enumerate(nums):
            sliced = nums[:i]+nums[i+1:] # 1 4 6
            output.append(prod(sliced))
        return output

