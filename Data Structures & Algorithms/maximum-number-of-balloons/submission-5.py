class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        have = Counter(text)
        for c in have:
            if c == "l" or c == "o":
                have[c] //= 2
        return min(have[c] for c in "balon")
        


        