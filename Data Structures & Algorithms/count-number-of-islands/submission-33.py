class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        def bfs(a, b):
            queue = deque()
            queue.append((a, b))
            grid[a][b] = "0"
            while queue:
                nc, nn = queue.popleft()
                for rc, rn in [(1,0), (-1, 0), (0,-1), (0,1)]:
                    row = rc + nc
                    col = rn + nn
                    if 0<= row < rows and 0<= col < cols and grid[row][col] == "1":
                        grid[row][col] = "0" 
                        queue.append((row, col))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        return count