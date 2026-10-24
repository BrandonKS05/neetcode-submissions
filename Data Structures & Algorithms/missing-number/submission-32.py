class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count =0
        n = len(nums)
        ideal = n*(n+1)/2
        total = sum(nums)
        return int(ideal - total)
        