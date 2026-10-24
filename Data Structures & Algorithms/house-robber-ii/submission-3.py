class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def linearsearch(house):
            prev1 = 0
            prev2 = 0
            for num in house:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1
        return max(linearsearch(nums[:-1]), linearsearch(nums[1:]))
            
