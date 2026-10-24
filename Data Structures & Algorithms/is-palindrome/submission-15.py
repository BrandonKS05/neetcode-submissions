class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = []
        for a in s:
            if a.isalnum():
                newstring.append(a.upper())
        if "".join(reversed(newstring)) == "".join(newstring):
            return True
        else:
            return False
       

        
        
