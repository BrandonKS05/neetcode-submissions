class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(parenthesis, opened, closed):
            if len(parenthesis) >= 2 * n:
                res.append(parenthesis)
                return

            if opened < n:
                backtrack(parenthesis + '(', opened + 1, closed)
            
            if closed < opened:
                backtrack(parenthesis + ')', opened, closed + 1)
               
        backtrack("", 0, 0)
        return res
        