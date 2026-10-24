class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        def dfs(a, b):
            if a >= 0 and  b >= 0 and a< rows and b < cols and grid[a][b]== "1":
                grid[a][b] = "0"
                dfs(a - 1, b)
                dfs(a + 1, b)
                dfs(a, b +1)
                dfs(a, b -1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count