class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        freq = [0] * (rows * rows)
        res = [-1, -1]
        for i in range(rows):
            for j in range(cols):
                idx = ord(chr(grid[i][j])) - ord(chr(1))
                
                freq[idx] += 1
        for i in range(len(freq)):
            if freq[i] == 2:
                res[0] = i + 1
            if freq[i] == 0:
                res[1] = i + 1
        return res

        