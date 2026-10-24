class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        output = []
        q = {}
        for num in nums:
            if num in q:
                q[num] = q[num]+1
            else:
                q[num] = 1
        ordered_list=q.items()
        my_new = sorted(ordered_list, key = lambda x: x[1],reverse = True)
        for stuff in my_new[:k]:
            output.append(stuff[0])
        return output

    
            

        
                


            

        

       
        