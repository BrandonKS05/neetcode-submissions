class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = -(heapq.heappop(heap))
            y = -(heapq.heappop(heap))

            if x != y:
                smaller = max(x,y) - min(x, y)
                heapq.heappush(heap, -(x-y))
        return 0 if not heap else -heapq.heappop(heap)





        