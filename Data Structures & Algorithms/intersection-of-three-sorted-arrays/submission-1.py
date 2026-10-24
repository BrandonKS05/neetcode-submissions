class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        seen = {}
        res = []
        for num in arr1:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        for num in arr2:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        for num in arr3:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
            if seen[num] == 3:
                res.append(num)
        return res

