class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak = 0
        numset = set(nums)
        for num in numset:
            y = num 
            while y in numset:
                y+= 1
                streak = max(streak, y - num)
        return streak