class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxvalue = set()
        best = 0
        j = 1
        for i in range(len(arr)):
            for num in range(j,len(arr)):
                best = max(best, arr[num])
            arr[i] = best
            print(best)
            best = 0
            j += 1
            if i == len(arr)-1:
                arr[i] = -1
        return arr
            

            