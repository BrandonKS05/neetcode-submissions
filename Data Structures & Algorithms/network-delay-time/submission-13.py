class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i + 1: [] for i in range(n)}

        for node, neighbor, time in times:
            graph[node].append((neighbor, time))

        dist = {i + 1 : float('inf') for i in range(n)}

        dist[k] = 0
        myheap = [(k, 0)]

        while myheap:
            ui, time = heapq.heappop(myheap)
            if time > dist[ui]:
                continue
            for vi, ti in graph[ui]:
                if time + ti < dist[vi]:
                    dist[vi] = time + ti
                    heapq.heappush(myheap, (vi, dist[vi]))
                    
        min_time = max(dist.values())
        return -1 if min_time == float('inf') else min_time




