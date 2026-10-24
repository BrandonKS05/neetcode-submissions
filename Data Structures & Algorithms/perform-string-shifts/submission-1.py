class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        res = [strs for strs in s] 
        for r in shift:
            if r[0] == 0:
                for i in range(r[1]):
                    tmp = res[0]
                    res.remove(tmp)
                    res.append(tmp)
            
            elif r[0] == 1:
                for i in range(r[1]):
                    tmp = res.pop()
                    res.insert(0, tmp)
            print(res)
        ans = ""
        for strs in res:
            ans += strs
        return ans



    

        
        