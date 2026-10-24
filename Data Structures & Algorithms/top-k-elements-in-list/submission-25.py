class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= {}
    
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] -= 1

        num_count = [(count, num) for num, count in freq.items()]
        heapq.heapify(num_count)
           
        
        return [heapq.heappop(num_count)[1] for _ in range(k) ]

        





            
        