class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] -= 1

        lst = []
        for key, val in hashmap.items():
            lst.append((val, key))
       
        heapq.heapify(lst)
     
        return [heapq.heappop(lst)[1] for __ in range(k)]
            

            
        