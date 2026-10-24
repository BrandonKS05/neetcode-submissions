class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        count_row = [0] * len(grid)
        count_col = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count_row[i] += 1
                    count_col[j] += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                valid_row = count_row[i] > 1
                valid_col = count_col[j] > 1
                if grid[i][j] == 1 and (valid_row or valid_col):
                    res += 1
        
        return res



       

        