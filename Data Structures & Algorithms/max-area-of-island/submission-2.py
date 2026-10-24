class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == 0:
                return 0
            grid[row][col] = 0 
            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) +dfs(row, col - 1))
            return count
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count = dfs(row, col)
                    best = max(best, count)
        return best
        