class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_nodes = len(points)
        point = {i: (points[i][0], points[i][1]) for i in range(num_nodes)}
        parent = [i for i in range(num_nodes)]
        edges = []
        res, count = 0, 0
        

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = point[i][0], point[i][1]
                xf, yf = point[j][0], point[j][1]
                dist = abs(yf - yi) + abs(xf-xi)
                
                edges.append((i, j, dist))
        
        edges.sort(key = lambda x: x[2])
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            
            if root_u == root_v:
                return False
            parent[root_u] = root_v
            return True

        for u, v, cost in edges:
            if union(u, v):
                res += cost
                count += 1

            if count == num_nodes - 1:
                break
        return res
                



        