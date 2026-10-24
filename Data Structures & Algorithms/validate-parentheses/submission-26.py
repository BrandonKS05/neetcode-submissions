class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {")" : "(","}" : "{", "]" : "["}
        seen = []
        for char in s:
            if char in paranthesis:
                if not seen:
                    return False
                if paranthesis[char] != seen[-1]:
                    return False
                seen.pop()
            else:
                seen.append(char)
        return len(seen) == 0
    
        


