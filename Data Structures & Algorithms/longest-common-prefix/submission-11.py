class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        newlist = []
        minstring = min(strs, key=len)
        if not strs:
            return ""
        newstrs = [poop for poop in strs]
        for col in range(len(minstring)):
            char = newstrs[0][col]
            for row in range(1,len(newstrs)):
                if newstrs[row][col] != char:
                    return "".join(newlist)
            newlist.append(char)
        return "".join(newlist)


                    
                
                

        


