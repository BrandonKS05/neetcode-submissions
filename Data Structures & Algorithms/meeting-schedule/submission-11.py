"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
            sorted_num = sorted(intervals, key = lambda x: x.start)
            new = [(x.start, x.end) for x in sorted_num]
            print(new)
            n = len(intervals)
            for i in range(n):
                index = new[i][1]
                if i + 1 < n and index - new[i+1][0] > 0:
                    return False
            return True