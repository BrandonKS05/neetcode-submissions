class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_list = []
        for n in nums:
            if n in my_list:
                return True
            my_list.append(n)
        return False
        
            