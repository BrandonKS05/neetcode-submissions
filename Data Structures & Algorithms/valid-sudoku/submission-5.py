class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            filtered_row = [cell for cell in row if cell != "."]
            if len(filtered_row) != len(set(filtered_row)):
                return False
        for col in range(9):
            filtered_col = [board[row][col] for row in range(9) if board[row][col] != "."]
            if len(filtered_col) != len(set(filtered_col)): 
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




    

            



