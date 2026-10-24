class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        strings = []
        answer = []
        hashset = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    strings.append(words[i])
        for string in strings:
            if string not in hashset:
                answer.append(string)
            hashset.add(string)
        return answer



        