class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best = up = down = 1
        for x, y in zip(nums, nums[1:]):
            up, down = up * (y > x) + 1, down * (y < x) + 1
            best = max(best, up, down)
        return best
        
       