class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {')':"(", "}":"{","]":"["}
        stack = []
        for string in s:
            if string not in parenthesis:
                stack.append(string)
            else:
                if not stack:
                    return False
                if parenthesis[string] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
           
            
            


        