class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for string in s:
            if string.isalnum():
                clean += string
        print(("".join(list(reversed(clean)))).lower())
        return "".join(list(reversed(clean))).lower() == clean.lower()
        