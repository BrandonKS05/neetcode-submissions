class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {} #{act: [act, cat]}
        
        for s in strs:
            if "".join(sorted(s)) not in group:
                group["".join(sorted(s))] = []
        for s in strs:
            if "".join(sorted(s)) in group:
                group["".join(sorted(s))].append(s)
        return list(group.values())
                
            
            

        
        
        