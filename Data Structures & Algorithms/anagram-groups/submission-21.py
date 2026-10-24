class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {} 
        for s in strs:
            sortedstring = "".join(sorted(s))
            if sortedstring not in group:
                group[sortedstring] = []
            group[sortedstring].append(s)
        return list(group.values())
                
            
            

        
        
        