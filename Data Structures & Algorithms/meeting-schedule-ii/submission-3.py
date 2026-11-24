"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        # need to reuse meetings
        heap = []
        res=0
        for i in intervals:
            if heap and heap[0] <= i.start:
                heapq.heapreplace(heap, i.end)
            else:
                res+=1
                heapq.heappush(heap, i.end)
        return res