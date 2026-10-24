class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = 1
        max_prod = 1
        result = max(nums)
        for n in nums:
            tmp = max_prod * n
            max_prod = max(n, min_prod* n, max_prod * n )
            min_prod = min(n, min_prod* n, tmp)
            
            result = max(result, max_prod)
        return result

     



