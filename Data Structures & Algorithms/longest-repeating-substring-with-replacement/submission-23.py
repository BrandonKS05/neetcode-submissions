class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0]*26
        best = 0
        max_freq = 0
        l = 0
        for i in range(n):
            idx = ord(s[i]) - ord('A')
            freq[idx] += 1
            max_freq = max(max_freq, freq[ord(s[i])- ord("A")])
            cur = i - l + 1
            while cur - max_freq > k:
                idx = ord(s[l]) - ord('A')
                freq[idx] -= 1
                l += 1
                cur -= 1
            best = max(best, cur)
        return best
            


