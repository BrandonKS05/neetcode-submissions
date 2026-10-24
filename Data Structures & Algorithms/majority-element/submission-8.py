class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap= {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        return max(hashmap, key = hashmap.get)