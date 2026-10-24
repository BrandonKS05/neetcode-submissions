class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n1, n2 = len(sentence1), len(sentence2)

        if n1 != n2:
            return False

        similar = set()
        for pair in similarPairs:
            a, b = pair
            similar.add((a,b))
            similar.add((b, a))

        for i in range(n1):
            if sentence1[i] != sentence2[i]:
                if (sentence1[i], sentence2[i]) not in similar:
                    return False
        return True
                

