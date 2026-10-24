class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        adj = [[] for __ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = set()
        def dfs(node, previous):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == previous:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        return dfs(0, -1) and n == len(visited)
        
