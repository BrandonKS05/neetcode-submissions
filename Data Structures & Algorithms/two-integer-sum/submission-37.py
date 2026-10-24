class Solution:
    def twoSum(self, nums: List[int], target: int, _solve=lambda nums, target: next([i, j] for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i]+nums[j] == target)) -> List[int]:
        return _solve(nums, target)