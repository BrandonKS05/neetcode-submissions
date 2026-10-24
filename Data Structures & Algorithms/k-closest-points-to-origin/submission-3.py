class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mst = []
        edges = []
        sets = [{(0, 0)}]

        for xi, yi in points:
            sets.append({(xi, yi)})

        for xi, yi in points:
            dist = ((xi ** 2) + (yi ** 2))**0.5
            edges.append((dist, (0, 0), (xi, yi)))
        
        edges.sort(key = lambda x: x[0])

        print(sets)

        print(edges)

        for dist, origin, neighbor in edges:

            for c in sets:
                if origin in c:
                    corigin = c
                    break

            for c in sets:
                if neighbor in c:
                    cneighbor = c
                    break
            
            if corigin is not cneighbor:
                corigin |= cneighbor
                sets.remove(cneighbor)
                mst.append(neighbor)
        
        return list(mst[:k])




        