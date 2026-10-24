class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False

        c = [0] * 26

        for i in range(n1):
            idx = ord(s[i]) - ord('a')
            c[idx] += 1

            idx = ord(t[i]) - ord('a')
            c[idx] -= 1
        
        for num in c:
            if num != 0:
                return False
        return True

        