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
                last = stack[-1]
                if parenthesis[string] == last:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
           
            
            


        