class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        local = []

        def isPalindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            if i == len(s):
                res.append(local.copy())
                return
            for cur in range(i, len(s)):
                if isPalindrome(s, i, cur):
                    local.append(s[i: cur + 1])
                    backtrack(cur + 1)
                    local.pop()
            return 
        
        backtrack(0)
        return res

