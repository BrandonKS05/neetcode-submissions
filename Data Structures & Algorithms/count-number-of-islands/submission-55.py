class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        
        queue = deque()
        def bfs(r, c):
            queue.append((i, j))
            while queue:
                r, c = queue.pop()
                grid[r][c] = "0"
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if r + dr < 0 or r + dr >= len(grid) or c + dc < 0 or c + dc >= len(grid[0]):
                        continue
                    if grid[r + dr][c + dc] == "0":
                        continue
                    queue.append((r + dr, c + dc))
                

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        return res



        