class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return True if nums == sorted(nums) else True if nums == sorted(nums, reverse = True) else False
        