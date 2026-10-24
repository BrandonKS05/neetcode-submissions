class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
    
        parent = {}
        count = 0
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]
        
        def union(x, y):
            nonlocal count
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                count -= 1  
        
      
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    parent[(r, c)] = (r, c)  
                    count += 1
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nr, nc = r + dr, c + dc
                        if (nr, nc) in parent:
                            union((r,c), (nr,nc))
        
        return count