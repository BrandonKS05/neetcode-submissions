class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        seen = set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            
            best = max(best, i - l + 1)
            seen.add(s[i])  
        
        return best

        