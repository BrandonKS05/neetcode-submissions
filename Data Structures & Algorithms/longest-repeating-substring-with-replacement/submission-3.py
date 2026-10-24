class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        best = 0
        counter = [0] * 26
        max_frequency = 0
        for r in range(len(s)):
            index = ord(s[r]) - ord("A")
            counter[index] += 1
            max_frequency = max(max_frequency, counter[index])
            while r - l + 1 - max_frequency > k:
                left_index = ord(s[l]) - ord("A")
                counter[left_index] -= 1
                l += 1
            best = r - l + 1
        return best




