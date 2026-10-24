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
                if dr + r < 0 or dc + c < 0 or dr + r >= len(grid) or dc + c >= len(grid[0]):
                    continue
                if grid[dr + r][dc + c] != 1:
                    continue

                grid[dr + r][dc + c] = 2
                queue.append((dr + r, dc + c, day + 1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        else:
            return best
                



        