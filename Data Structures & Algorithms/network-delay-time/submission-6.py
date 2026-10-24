class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        dist = {}
        
        for node, neighbor, time in times:
            graph[node].append((neighbor, time))
        
        for node in graph:
            dist[node] = float('inf')
        
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
        greatest = float('inf')
        for time in dist.values(): 
            if time == greatest:
                return -1
        return max(dist.values())

        