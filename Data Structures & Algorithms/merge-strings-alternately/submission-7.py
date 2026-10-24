class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxword = max(word1, word2, key = len)
        minword = min(word1, word2, key = len)
        newlist = []
        for i in range(len(minword)):
            newlist.append(word1[i] + word2[i])
        for j in range(len(minword), len(maxword)):
            newlist.append(maxword[j])
        return "".join(newlist)
        
       

        