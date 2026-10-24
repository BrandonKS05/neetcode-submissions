class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        s = hashmap.items()
        print(s)
        print(hashmap)
        newlist = sorted(s, key = lambda x: x[0], reverse = True)
        print(newlist)
        for a in newlist:
            if a[1] == 1:
                return a[0]
        return -1
            

        