class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        sets = [{(xi,yi)} for xi, yi in points]
        total_dist = 0

        for i in range(len(points)):
            for j in range(i + 1, len(points)):

                xi, yi = points[i]
                xj, yj = points[j]

                dist = abs(xi - xj) + abs(yi - yj)

                edges.append((dist, (xi, yi), (xj, yj)))

        edges.sort(key = lambda x: x[0])

        for dist, u, v in edges:
            
            for c in sets:
                if u in c:
                    cu = c
                    break
            
            for c in sets:
                if v in c:
                    cw = c
                    break
                
            if cu is not cw:
                cu |= cw
                sets.remove(cw)
                total_dist += dist
                
        return total_dist


        

            