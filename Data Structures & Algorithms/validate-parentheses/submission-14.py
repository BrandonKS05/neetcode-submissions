class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        all_bracket = {"]":"[", "}":"{", ")":"("}

        for char in s:
            if char in all_bracket:
                if stack:
                    pass
                else:
                    return False
                top_stuff = stack.pop()
                if top_stuff != all_bracket[char]:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else: 
            return False

