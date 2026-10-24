class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for string in s:
            if string.isalnum():
                cleaned  = cleaned + string.lower()
        return cleaned == ''.join(reversed(cleaned))
