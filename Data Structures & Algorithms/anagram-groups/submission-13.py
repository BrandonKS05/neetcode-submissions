class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for strings in strs:
            newstring = ("".join(sorted(strings)))
            if newstring not in seen:
                seen[newstring]=[]
            seen[newstring].append(strings)
        output = []
        for value in seen:
            output.append(seen[value])
        print(output)
        return output