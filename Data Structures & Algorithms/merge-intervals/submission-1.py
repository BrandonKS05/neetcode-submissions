class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        print(intervals)
        newlist = []
        i = 0
        n = len(intervals) 
        while i < n:
            if i < n - 1 and intervals[i][1] < intervals[i+1][0]:
                newlist.append(intervals[i])
                i += 1
            elif i < n - 1 and intervals[i+1][0] <= intervals[i][1]:
                intervals[i+1][0] = min(intervals[i+1][0], intervals[i][0])
                intervals[i+1][1]= max(intervals[i+1][1], intervals[i][1])
                i += 1
            else:
                newlist.append(intervals[i])
                i += 1
        return newlist
                
        
    #[1,2][3,4][5,8][6,10][6,7][14,15]
    #[5,8][5,10][5,10]