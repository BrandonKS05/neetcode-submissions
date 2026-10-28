class Solution:
    def isValid(self, s: str) -> bool:
        z = {"}": "{", "]": "[", ")": "("}
        stack = []

        for i in range(len(s)):
            if s[i] in z:
                if not stack:
                    return False
                else:
                    if stack[-1] != z[s[i]]:
                        return False
                    else:
                        stack.pop()
            else:
                stack.append(s[i])
        return False if stack else True
        