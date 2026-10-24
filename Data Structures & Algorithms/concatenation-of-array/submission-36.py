class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        hashmap1 = {}
        n = len(nums)
        for i in range(len(nums)):
            hashmap1.setdefault(i, None)
      
        print(hashmap1)
        res = [0] * 2 * n
        print(res)
        for key in hashmap1:
            res[key] = nums[key]
            res[key + n] = nums[key]
        return res
      

            
       

        