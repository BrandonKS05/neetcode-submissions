class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        rank = [0] * n
        parent = list(range(n))
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        for u, v in edges:
            if not union(u, v):
                return False
        return True
        

