class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        counter = 0
        adj = [[] for i in range(n)]
        visited = set()
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
            return
        for node in range(n):
            if node not in visited:
                counter += 1
                dfs(node)
        return counter
        
