from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i,num in enumerate(nums):
            sliced = nums[:i]+nums[i+1:]
            output.append(reduce(lambda x,y:x*y,sliced))
        return output

