class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += (str(len(word)))
            res += ("#")
            res += (word)
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            start, end = j, j + length
            res.append(s[start: end])
            i = end   
        return res
