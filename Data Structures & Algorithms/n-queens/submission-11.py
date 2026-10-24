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

        def check(row, col):
            in_across = col in cols
            in_diagonal = row - col in diagonal or row + col in anti 

            return False if in_across or in_diagonal else True
               
        def backtrack(i):
            if i >= n:
                res.append([pos[:col] + "Q" + pos[col + 1:] for col in board])
                return
            
            for j in range(n):
                if check(i, j):
                    track(i, j, True)

                    board.append(j)
                    backtrack(i + 1)

                    track(i, j, False)
                    board.pop()

        backtrack(0)

        return res


                

            
        


     