class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)
        row = 0
        while row < rows:
            word1 = ""
            for i in range(rows):
                if row < len(words[i]):
                    word1 += words[i][row]
            if word1 != words[row]:
                return False
            row += 1

        return True