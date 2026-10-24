from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # prefix pass: output[i] = product of all elements left of i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # suffix pass: multiply by product of all elements right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output

