class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_frequency = 0
        best = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord("A")] += 1
            max_frequency = max(max_frequency, count[ord(s[right]) - ord("A")])
            while right - left - max_frequency + 1> k:
                count[ord(s[left]) - ord("A")] -=1
                left += 1
        best = right - left + 1
        return best

        
