class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        for i in range(n + 1):
            if start not in nums:
                return start
            start += 1




   
