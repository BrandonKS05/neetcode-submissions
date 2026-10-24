class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for row in board:
            seen = set()
            for i in range(n):
                if row[i] != "." and row[i] in seen:
                    return False
                seen.add(row[i])

        for i in range(n):
            seen = set()
            for j in range(n):
                if board[j][i] != "." and board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        subgrid = board[i + start_row][j + start_col]
                        if subgrid != "." and subgrid in seen:
                            return False
                        seen.add(subgrid)
               
        return True
        