from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i,num in enumerate(nums):
            sliced = nums[:i]+nums[i+1:]
            output.append(prod(sliced))
        return output

