class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)
        #1 + 2 + 3 + 4 ... + n = s
        #n + (n-1) + (n - 2) ... + 1 = s
        #(n+1) + (n+1) ... (n+1) = 2s
        #(n+1)*n = 2s
        #s = (n+1)*n/2