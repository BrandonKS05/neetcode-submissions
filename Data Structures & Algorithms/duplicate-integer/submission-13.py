class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in nums:
            if nums.count(x) >= 2:
                return True
        return False
