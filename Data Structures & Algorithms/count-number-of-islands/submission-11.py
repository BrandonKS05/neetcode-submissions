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
                row, col = queue.popleft();
                for nr, cr in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    nd = row + nr
                    nc = col +cr
                    if 0 <= nd < rows and 0 <= nc < cols and grid[nd][nc] == "1":
                        queue.append((nd, nc))
                        grid[nd][nc] = "0"
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    count += 1
                    bfs(x, y)
        return count
