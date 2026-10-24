class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        
        for node, neighbor, time in times:
            graph[node].append((neighbor, time))
        
        dist = {i: float('inf') for i in range(1, n + 1)}
        
        dist[k] = 0
        myheap = [(0, k)]
    
        while myheap:
            time, node = heapq.heappop(myheap)
            if time > dist[node]:
                continue
            for vi, ti in graph[node]:
                if time + ti < dist[vi]:
                    dist[vi] = time + ti
                    heapq.heappush(myheap,(dist[vi],vi))

        greatest = max(dist.values())
        return -1 if greatest == float('inf') else greatest
                
 

        