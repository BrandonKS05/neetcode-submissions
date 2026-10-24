class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = [0] * 26
        left = 0
        best = 0
        max_frequency = 0
        for i in range(len(s)):
            char[ord(s[i])- ord("A")] += 1
            max_frequency = max(max_frequency, char[ord(s[i])- ord("A")])
            while i - left - max_frequency + 1 > k:
                char[ord(s[left])- ord("A")] -= 1
                left += 1
        best = i - left + 1
        return best
