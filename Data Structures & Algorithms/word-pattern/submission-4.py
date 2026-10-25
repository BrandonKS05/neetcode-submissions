class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        f1, f2 = {}, {}
        for i in range(len(pattern)):
            x = pattern[i]
            y = words[i]
            
            if x in f1 and f1[x] != y:
                return False
            if y in f2 and f2[y] != x:
                return False
            
            f1[x] = y
            f2[y] = x
        return True
      



        