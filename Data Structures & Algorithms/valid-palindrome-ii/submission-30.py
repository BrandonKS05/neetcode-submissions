class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(strs):
            l = 0
            r = len(strs) - 1
            while l < r:
                if strs[l] != strs[r]:
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                l_removed = isPalindrome(s[:l] + s[l+1:])
                r_removed = isPalindrome(s[:r]+ s[r+1:])
                return l_removed or r_removed
            l += 1
            r -= 1
        return True

                
            
            