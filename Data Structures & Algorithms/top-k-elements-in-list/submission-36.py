class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
     
        l = []
        for key, val in freq.items():
            l.append((key,val))
        
        l.sort(key = lambda x: x[1], reverse = True)
       
        return [l[i][0] for i in range(k)]


        