"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 1:
            return 1
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)
        count = 0 
        dp = [False] * n
        for i in range(n):
            if dp[i]:
                continue
            cur_end = intervals[i].end
            for j in range(i + 1, n):
                if not dp[j] and intervals[j].start >= cur_end:
                    dp[j] = True
                    cur_end = intervals[j].end
            count += 1
        return count
        