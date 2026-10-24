class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a, b = word1, word2
        m = len(a)
        if m == 0:
            return len(b)
        mask = (1 << m) - 1
        top = 1 << (m - 1)

        # peq[c]: bit i set when a[i] == c
        peq = {}
        for i, ch in enumerate(a):
            peq[ch] = peq.get(ch, 0) | (1 << i)

        vp, vn = mask, 0          
        score = m             
        for ch in b:
            eq = peq.get(ch, 0)
            d0 = ((((eq & vp) + vp) & mask) ^ vp) | eq | vn  
            hp = vn | (~(d0 | vp) & mask)                  
            hn = vp & d0                                  
            if hp & top:
                score += 1
            elif hn & top:
                score -= 1
            hp = ((hp << 1) | 1) & mask  
            hn = (hn << 1) & mask
            vp = hn | (~(d0 | hp) & mask)
            vn = hp & d0
        return score

 

