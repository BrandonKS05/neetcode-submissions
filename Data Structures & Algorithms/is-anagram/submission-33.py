class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        counter = [0] * 26
        l = 0
        while l < n:
            index = ord(s[l]) - ord('a') 
            counter[index] += 1
            index = ord(t[l]) - ord('a') 
            counter[index] -= 1
            l += 1
        for num in counter:
            if num != 0:
                return False
        return True

        
