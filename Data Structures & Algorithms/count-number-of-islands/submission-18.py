from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        def bfs(a, b):
            queue = deque()
            queue.append((a,b))
            grid[a][b] = "0"
            while queue:
                row, col = queue.popleft()
                for nc, nr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dc = row + nc
                    dr = col + nr
                    if 0 <= dc < rows and 0<= dr < cols and grid[dc][dr] == "1":
                        queue.append((dc,dr))
                        grid[dc][dr] = "0"
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        return count