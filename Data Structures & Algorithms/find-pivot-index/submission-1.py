class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        for i in range(len(nums)):
            leftsum, rightsum = sum(nums[:i]), sum(nums[i + 1:])
            if leftsum == rightsum:
                return i
        return -1
            




        