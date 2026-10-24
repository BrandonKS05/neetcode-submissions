class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        best = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        while queue:
            r, c, day = queue.popleft()
            best = max(best, day)

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                queue.append((nr, nc, day + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return best