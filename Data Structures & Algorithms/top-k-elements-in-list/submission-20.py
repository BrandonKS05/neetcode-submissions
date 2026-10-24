class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= {}
        num_count = []
        

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        for num, count in freq.items():
            num_count.append((-count, num))
            
        heapq.heapify(num_count)
        
        return [heapq.heappop(num_count)[1] for _ in range(k) ]

        





            
        