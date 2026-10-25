class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        local, best, prev = 0, 0, -1
        for num in nums:
            if prev >= num:
                local, prev = num, num
                
            else:
                local += num
                best, prev = max(best, local), num
        return best
        