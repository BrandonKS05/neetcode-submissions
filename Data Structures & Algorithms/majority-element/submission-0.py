class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap= {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        a = (list(hashmap.items()))
        sortlist = sorted(a, key = lambda x: x[1], reverse = True)
        return sortlist[0][0]
