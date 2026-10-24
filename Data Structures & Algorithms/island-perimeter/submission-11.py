class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(a, b):
            if a >= len(grid) or a < 0 or b >= len(grid[0]) or b < 0:
                return 1

            if grid[a][b] == 0:
                return 1
                
            if grid[a][b] == -1:
                return 0

            grid[a][b] = -1
            
            up = dfs(a, b + 1) 
            down = dfs(a, b - 1)
            right = dfs(a + 1, b) 
            left = dfs(a - 1, b) 

            return up + down + right + left
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0    
            
    
                

           


            
        