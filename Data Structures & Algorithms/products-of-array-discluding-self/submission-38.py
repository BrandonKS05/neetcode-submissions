class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # Initialize output list with 1's

        # First pass: Calculate left products (product of all elements to the left of current index)
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]  # Update left product for the next index
        
        # Second pass: Calculate right products and combine with left products
        right = 1
        for i in range(n - 1, -1, -1):  # Iterate backwards
            output[i] *= right  # Multiply by the right product
            right *= nums[i]  # Update right product for the next index
        
        return output
