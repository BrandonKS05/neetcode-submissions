class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        tmp = []
        tmp.append(word1)
        tmp.append(word2)
        maxword = max(tmp, key = len)
        minword = min(tmp, key = len)
        newlist = []
        for i in range(len(minword)):
            newlist.append(word1[i] + word2[i])
        for j in range(len(minword), len(maxword)):
            newlist.append(maxword[j])
        return "".join(newlist)
        
       

        