class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        
        hashmap = {'2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
       
        def backtrack(i, stack):
            if i >= len(digits):
                sol = "".join(stack)
                res.append(sol)
                return

            for ch in (hashmap[digits[i]]):
                stack.append(ch)
                backtrack(i + 1, stack)
                stack.pop()

        backtrack(0, [])
        return res

            
            
            


        