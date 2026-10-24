class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def checkSubstring(string1, string2):
            freq = [0] * 26
            for i in range(len(s1)):
                idx = ord(string1[i]) - ord('a')
                freq[idx] += 1
                idx = ord(string2[i]) - ord('a')
                freq[idx] -= 1
            for num in freq:
                if num !=0:
                    return False
            return True


        for i in range(len(s1) - 1, len(s2)):
            if s2[i] in s1:
                print(s2[i - len(s1) + 1 :i + 1])
                if checkSubstring(s1, s2[i - len(s1) + 1:i + 1]):
                    return True
        return False
                


        