class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod, max_prod = 1, 1
        result = max(nums)
        for n in nums:
            max_prod, min_prod = max(n, min_prod* n, max_prod * n ), min(n, min_prod* n, max_prod *n)
            result = max(result, max_prod)
        return result

     



