class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        local = 0
        best = 0
        prev = -1
        for num in nums:
            if prev >= num:
                local = 0
            local += num
            print(local)
            best = max(best, local)
            prev = num
        return best
        