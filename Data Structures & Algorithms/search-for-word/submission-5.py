class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def dfs(a, b, i):
            if i == len(word):
                return True
            if a < 0 or a >= rows:
                return False
            if b < 0 or b >= cols:
                return False
            if board[a][b] == "#":
                return False
            if board[a][b] != word[i]:
                return False
            tmp = board[a][b]
            board[a][b] = "#"
            found = dfs(a - 1, b, i + 1) or dfs(a + 1, b, i + 1) or dfs(a, b - 1, i + 1) or dfs(a, b + 1, i + 1)
            board[a][b] = tmp
            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False