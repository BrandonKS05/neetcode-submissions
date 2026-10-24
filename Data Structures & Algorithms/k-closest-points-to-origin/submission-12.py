class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dot = []
        
        for xi, yi in points:
            dist = xi**2 + yi ** 2
            heapq.heappush(dot, [-dist, xi, yi])
            if len(dot) > k:
                heapq.heappop(dot)
            

        return [[xi, yi] for dist, xi, yi in dot]
