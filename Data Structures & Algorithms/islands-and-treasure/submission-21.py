class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasure = 0
        water = -1
        land = 2147483647
        

        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == treasure:
                    queue.append((i,j, 0))

        while queue:
            r, c, step = queue.popleft()


            for dr, dc in [(-1, 0), (1,0), (0, -1), (0, 1)]:
                row,  col = r + dr, c + dc

                valid_row = row >= 0 and row < len(grid)
                valid_col = col >= 0 and col < len(grid[0])

                if valid_row and valid_col and grid[row][col] == land:
                    
                    grid[row][col] = step + 1
                    queue.append((row, col, step + 1))
                


        

            
            


                



        