class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        marc = 0
        for num in nums:
            marc ^= num
        
        for i in range(len(nums) + 1):
            marc ^= i
        
        return marc
        




   
