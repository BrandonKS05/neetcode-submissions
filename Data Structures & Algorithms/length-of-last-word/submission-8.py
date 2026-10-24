class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1 
        if len(s) == 1 and s != " ":
            return 1
        count = 0
        while s[r] == " ":
            r -= 1
        print(r)
        end = r
        while s[r]!= " " and r > 0:
            r -= 1
        print(r)
        start = r
        return end - start
        
        

            
        