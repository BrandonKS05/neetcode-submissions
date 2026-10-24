class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = []
        for a in s:
            if a.isalnum():
                newstring.append(a.upper())
        z = "".join(reversed(newstring))
        x = "".join(newstring)
        if x == z:
            return True
        else:
            return False
       

        
        
