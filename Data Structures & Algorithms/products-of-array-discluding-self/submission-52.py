class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left  = [1] * n
        right = [1] * n
        for i in range(n-1):
            left[i+1] = left[i]*nums[i]
        for i in range(n-1,0,-1):
            right[i-1] = right[i]*nums[i]
        for i in range(n):
            left[i] = left[i]*right[i]
        return left

            