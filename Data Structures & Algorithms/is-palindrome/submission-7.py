class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=list(s)
        #remove all non alphanumerical stuff
        temp = []
        for char in a:
            if char.isalnum():
                temp.append(char)
        a = temp

        #lowercase everything

        a=[char.lower() for char in a]
    
        #create a new list called b
    
        b =[]
        for char in a:
            b.append(char)
        #reverse a and compare
        a.reverse()
        if a == b:
            return True
        return False
       

        
        
