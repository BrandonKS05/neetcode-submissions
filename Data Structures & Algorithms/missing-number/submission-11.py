class Solution:
    def missingNumber(self, nums: List[int]) -> int:
            n = len(nums)
            xor = -1
            for i in range(n + 1):
                xor = xor ^ i
            xor = xor ^ -1
            for num in nums:
                xor = xor ^ num
            return xor
                