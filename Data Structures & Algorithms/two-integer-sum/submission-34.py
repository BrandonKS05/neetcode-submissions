class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            need = target - nums[i] 
            if need in dictionary:
                return [dictionary[need], i]
            dictionary[nums[i]] = i

        