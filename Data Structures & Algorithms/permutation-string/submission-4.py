class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def is_permutation(window):
            return sorted(window) == sorted(s1)
            return 
            for s in s1:
                if s in window:
                    counter -= 1
            return True if counter == 0 else False
        n1 = len(s1) - 1 
        n2 = len(s2) - 1
        for i in range(n2 + 1):
            r = i 
            if s2[i] in s1 and r + n1 <= len(s2):
                print(s2[i:r + n1 + 1])
                tmp = is_permutation(s2[i:r + n1 + 1])
                if tmp: 
                    return True
        return False
    



        
       

               