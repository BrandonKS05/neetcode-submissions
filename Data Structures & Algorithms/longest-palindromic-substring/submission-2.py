class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        start = 0
        max_len = 0
        def expand(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            length = max(odd, even)
            if length > max_len:
                max_len = length
                start = i - (max_len - 1)//2
        return s[start: start + max_len]
        
        
        

    