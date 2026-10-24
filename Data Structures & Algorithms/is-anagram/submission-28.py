class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = [0] * 26
        for string in s:
            tracker[ord("a") - ord(string)]+= 1
        for string in t:
            tracker[ord("a") - ord(string)]-= 1
        for num in tracker:
            if num != 0:
                return False
        return True
