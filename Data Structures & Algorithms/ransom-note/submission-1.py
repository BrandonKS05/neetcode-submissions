class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = [0] * 26
        for c in magazine:
            idx = ord(c) - ord('a')
            freq[idx] += 1
            
        for c in ransomNote:
            idx = ord(c) - ord('a')
            freq[idx] -= 1
        
        for num in freq:
            if num < 0:
                return False
        return True
         
        