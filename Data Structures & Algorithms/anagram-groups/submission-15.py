class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        output = []
        for strings in strs:
            newstring = ("".join(sorted(strings)))
            if newstring not in seen:
                seen[newstring]=[]
            seen[newstring].append(strings)
        return (list(seen.values()))
       