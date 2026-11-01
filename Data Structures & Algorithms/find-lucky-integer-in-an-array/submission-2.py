class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen = {}
        res = []
        for num in arr:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        
        for key, val in seen.items():
            if key == val:
                res.append(key)


        return -1 if not res else max(res)

        