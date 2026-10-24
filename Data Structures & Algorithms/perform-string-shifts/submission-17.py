class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net = 0
        for r in shift:
            if r[0] == 0:
                net -= r[1]
            elif r[0] == 1:
                net += r[1]
        net %= len(s)
        if net <= 0:
            n = abs(net)
            s = s[n:] + s[:n]
        else:
            n = len(s) - net
            s = s[n:] + s[:n]
        return s
            
        



    

        
        