class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in hashmap:
                hashmap[sorted_string] = []
            hashmap[sorted_string].append(string)

        for key, val in hashmap.items():
            res.append(val)

        return res

            
            
            

        
        
        