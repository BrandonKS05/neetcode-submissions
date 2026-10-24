class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        counter = 0
        adj = [[] for i in range(n)]
        visited = set()
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        def dfs(node, previous):
            if node in visited:
                return
            visited.add(node)
            for j in adj[node]:
                dfs(j, node)
            return
        for i in range(n):
            if i not in visited:
                counter += 1
                dfs(i, -1)
        return counter
        
