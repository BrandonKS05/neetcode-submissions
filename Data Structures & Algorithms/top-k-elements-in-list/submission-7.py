class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        print(hashmap)
        clean = sorted((hashmap.items()), key = lambda x: x[1], reverse = True)
        return [s[0] for s in clean[:k]]

    

