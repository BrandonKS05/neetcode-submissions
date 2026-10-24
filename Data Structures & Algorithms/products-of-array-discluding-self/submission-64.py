class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        left_prod = 1
        for i in range(1, len(nums)):
            left_prod = left_prod * nums[i-1]
            left[i] = left_prod

      
        right_prod = 1
        for i in range(len(nums) - 2, -1, -1):
            right_prod = right_prod * nums[i + 1]
            right[i] = right_prod

        return [left[i] * right[i] for i in range(len(nums))]
        

           

        