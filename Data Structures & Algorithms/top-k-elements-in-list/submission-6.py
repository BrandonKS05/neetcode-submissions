class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        answer = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        print(hashmap)
        clean = sorted((hashmap.items()), key = lambda x: x[1], reverse = True)
        for s in clean[:k]:
            answer.append(s[0])
        return answer

