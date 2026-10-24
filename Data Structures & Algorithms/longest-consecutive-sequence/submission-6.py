class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        best = 0

        for num in nums:
            if num - 1 not in new_set:
                candidate = num
                local = 0

                while candidate in new_set:
                    local += 1
                    candidate += 1
                best = max(best, local)

        return best
          
            
            
           
        