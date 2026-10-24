class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net = 0
        for r in shift:
            if r[0] == 0:
                net -= r[1]
            
            elif r[0] == 1:
                net += r[1]
        net = net % len(s)
        if net <= 0:
            s = s[abs(net):] + s[:abs(net)]
        else:
            s = s[len(s) - net:] + s[:len(s) - net]
        return s
            
        



    

        
        