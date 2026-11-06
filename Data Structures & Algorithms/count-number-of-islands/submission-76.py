class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            grid[i][j] = "0"

            while queue:   
                r, c = queue.popleft()
              
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    row = dr + r
                    col = dc + c
                    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                        continue
                    if grid[row][col] == "0":
                        continue
                    if grid[row][col] == "1":
                        grid[row][col] = "0"
                        queue.append((row, col))
        
     
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                
                bfs(i, j)
                count += 1
                 

        return count