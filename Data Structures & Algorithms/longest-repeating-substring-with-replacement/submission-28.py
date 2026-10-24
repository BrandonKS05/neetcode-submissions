class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        max_freq = 0
        freq = [0] * 26
        l = 0
        for i in range(len(s)):
            idx = ord(s[i]) - ord('A')
            freq[idx] += 1
            max_freq = max(max_freq, freq[idx])

            while (i - l + 1) - max_freq > k:
                idx = ord(s[l]) - ord("A")
                freq[idx] -= 1
                l += 1
            best = max(best, i - l + 1)
        return best
                

     

            