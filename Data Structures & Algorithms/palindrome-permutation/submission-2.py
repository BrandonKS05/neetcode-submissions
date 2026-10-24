class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        seen = set()
        for strs in s:
            if strs in seen:
                seen.remove(strs)
            else:
                seen.add(strs)
        if len(seen) == 0 or len(seen) == 1:
            return True
        else:
            return False
    
        