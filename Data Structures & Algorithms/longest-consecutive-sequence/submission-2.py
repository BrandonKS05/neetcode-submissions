class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        new_nums = set(nums)

        for num in new_nums:
            if num-1 not in new_nums:
                y = num
                while y in new_nums:
                    y+=1
                    best = max(best, y-num)
        return best   
    

