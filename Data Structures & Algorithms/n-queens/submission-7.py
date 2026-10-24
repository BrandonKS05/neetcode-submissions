class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, diagonal, anti = set(), set(), set()
        board, res = [], []
        

        def track(row, col):
            cols.add(col)
            diagonal.add(row - col)
            anti.add(row + col)
            return

        def untrack(row, col):
            cols.remove(col)
            diagonal.remove(row - col)
            anti.remove(row + col)
            return

        def check(row, col):
            in_across = col in cols
            in_diagonal = row - col in diagonal or row + col in anti 
            return False if in_across or in_diagonal else True
               
        def backtrack(i):
            if i >= n:
                res.append(board.copy())
                return
            
            for j in range(n):
                if check(i, j):
                    track(i, j)
                    board.append(j)
                    backtrack(i + 1)
                    untrack(i, j)
                    board.pop()
            return

        backtrack(0)

        final = []
        for sol in res:
            tmp = []
            pos = "." * n
            for col in sol:
                row = pos[:col] + "Q" + pos[col + 1:]
                tmp.append(row)
            final.append(tmp)

        return final


                

            
        


     