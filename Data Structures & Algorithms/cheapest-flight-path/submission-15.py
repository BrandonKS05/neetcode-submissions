class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        
        for from_i, to_i, price_i in flights:
            graph[from_i].append((to_i, price_i))
        
        best_stops = {i: float('inf') for i in range(n)}

        best_stops[src] = 0
        queue = [(0, src, 0)]

        while queue:
            total, from_i, stops = heapq.heappop(queue)
            if from_i == dst:
                return total
            if stops > k or stops > best_stops[from_i]:
                continue
            best_stops[from_i] = stops
            for to_i, price_i in graph[from_i]:
                    heapq.heappush(queue, (total + price_i, to_i, stops + 1))
        return -1
        
        