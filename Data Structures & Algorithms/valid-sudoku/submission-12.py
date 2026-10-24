class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            newlist =[]
            for cell in row:
                if cell != ".":
                    newlist.append(cell)
            if len(newlist) != len(set(newlist)):
                return False
        for col in range(9):
            newlist_new = []
            for row in range(9):
                if board[row][col] != ".":
                    newlist_new.append(board[row][col])
            if len(newlist_new) != len(set(newlist_new)):
                return False
        for row in range(0, 9, 3):  
            for col in range(0, 9, 3):
                grid = []  
                for i in range(3): 
                    for j in range(3):  
                        if board[row + i][col + j] != ".": 
                            grid.append(board[row + i][col + j]) 
                if len(grid) != len(set(grid)): 
                    return False
        return True






    

            



