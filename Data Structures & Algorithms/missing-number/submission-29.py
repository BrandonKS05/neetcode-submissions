class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count =0
        for i in range(len(nums)):
            count += i +1
        total = sum(nums)
        return count - total 
        