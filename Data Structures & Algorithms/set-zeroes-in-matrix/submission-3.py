class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        is_first_row_zero = False
        is_first_col_zero = False

        for row in range(rows):
            if matrix[row][0] == 0:
                is_first_col_zero = True
        for col in range(cols):
            if matrix[0][col] == 0:
                is_first_row_zero = True


        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0


        for row in range(1, rows):
            if matrix[row][0] == 0:
                for n in range(cols):
                    matrix[row][n] = 0
        for col in range(1, cols):
            if matrix[0][col] == 0:
                for n in range(rows):
                    matrix[n][col] = 0
        
        if is_first_row_zero:
            for n in range(cols):
                matrix[0][n] = 0

        if is_first_col_zero:
            for n in range(rows):
                matrix[n][0] = 0
        
        


                

        