class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * 2 * n
        set1 = set()
        
        for i in range(len(nums)):
            set1.add(i)
   
        for key in set1:
            res[key] = nums[key]
            res[key + n] = nums[key]
        return res
      

            
       

        