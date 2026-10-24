class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for xi, yi in points:
            dist = ((xi ** 2) + (yi ** 2))**0.5
            heapq.heappush(heap, (-dist, xi, yi))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[xi,yi] for _, xi, yi in heap]
        
