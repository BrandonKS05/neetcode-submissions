class Solution:

    def encode(self, strs: List[str]) -> str:
        newlist = []
        for string in strs:
            newlist.append(str(len(string)))
            newlist.append("#")
            newlist.append(string)
        return "".join(newlist)
    def decode(self, s: str) -> List[str]:
        newwlist = []
        i=0
        while i<len(s):
            j=i
            while s[j]!= '#':
                j+=1
            length = int(s[i:j])
            j += 1
            newwlist.append(s[j:j+length])
            i = j + length
        return newwlist

