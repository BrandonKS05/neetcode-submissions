class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        need = {"b": 0, "a": 0, "l":0, "o":0, "n": 0}

        for c in text:
            if c in need:
                need[c] += 1
        res = 0
        while True:
            for c in need:
                
                if c == "l":
                    need[c] -= 1
                    
                if c == "o":
                    need[c] -= 1
                
                need[c] -= 1
                
                if need[c] < 0:
                    return res
            res += 1
        return res
            


        