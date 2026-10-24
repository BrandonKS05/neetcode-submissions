class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        parents = [i for i in range(n)]
        rank = [0] * n

        def find_parent(node):
            if node != parents[node]:
                node = find_parent(parents[node])
            return parents[node]
        
        def union(rootx, rooty):
            parent_x = find_parent(rootx)
            parent_y = find_parent(rooty)

            if parent_x == parent_y:
              return False

            if rank[parent_x] > rank[parent_y]:
                parents[parent_y] = parent_x
            
            if rank[parent_x] < rank[parent_y]:
                parents[parent_x] = parent_y

            if rank[parent_x] == rank[parent_y]:
                parents[parent_y] = parent_x
                rank[parent_x]+= 1
            return True
        
        for parent, child in edges:
            if not union(parent, child):
                return False
        return True






            



        
        