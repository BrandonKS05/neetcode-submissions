class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, diagonal, anti = set(), set(), set()
        board, res = [], []
        pos = "." * n
        

        def track(row, col, status):
            if status:
                cols.add(col)
                diagonal.add(row - col)
                anti.add(row + col)
            
            else:
                cols.remove(col)
                diagonal.remove(row - col)
                anti.remove(row + col)
               
        def backtrack(i):
            if i >= n:
                res.append([pos[:col] + "Q" + pos[col + 1:] for col in board])
                return
            
            for j in range(n):
                if j in cols or i - j in diagonal or i + j in anti:
                    continue
                
                track(i, j, True)
                board.append(j)
                backtrack(i + 1)

                track(i, j, False)
                board.pop()

        backtrack(0)

        return res


                

            
        


     