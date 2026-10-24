class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        res = nums[0]

        max_prod = 1
        min_prod = 1
        

        for num in nums:
            max_prod = max_prod * num
            min_prod = min_prod * num

            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(num, max_prod)
            min_prod = min(num, min_prod)

            res = max(res, max_prod)
        return res
               

        
      

        