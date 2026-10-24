class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1) 
        n2 = len(s2) 
       
        def is_permutation(window):
            freq = [0] * 26
            for i in range(n1):
                freq[ord(window[i]) - ord('a')] += 1
                freq[ord(s1[i]) - ord('a')] -= 1
            for num in freq:
                if num != 0:
                    return False
            return True

        for i in range(n2):
            r = i 
            if s2[i] in s1 and r + n1 <= len(s2):
                tmp = is_permutation(s2[i:r + n1])
                
                if tmp: 
                    return True
        return False
    



        
       

               