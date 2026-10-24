class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for string in s:
            if string.isalnum():
                clean += string
        clean = clean.lower()
        reverse = "".join(list(reversed(clean)))
        return reverse == clean
        