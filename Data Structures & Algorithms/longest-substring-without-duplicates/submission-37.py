class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        n = len(s)
        j = 0
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1
            seen.add(s[i])
            best = max(best, i - j + 1)
        return best