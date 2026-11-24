class Solution:
    def isOverlap(self, i1, i2):
        if i1[0] <= i2[0] <= i1[1]:
            return True
        return False

    def binarySearch(self, intervals, newInterval):
        """returns index to insert newInterval at"""
        l, r = 0, len(intervals) - 1
        startTarget = newInterval[0]
        while l <= r:
            m = (l + r) // 2
            start_m = intervals[m][0]
            if start_m == startTarget:
                return m
            elif start_m > startTarget:
                r = m - 1
            else:
                l = m + 1
        return l

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.sort()
        idx = self.binarySearch(intervals, newInterval)

        # Step 1: Insert at the found position
        intervals.insert(idx, newInterval)
        res = []
        curr = intervals[0]
        for i in intervals:
            if self.isOverlap(curr, i):
                curr = [min(i[0], curr[0]), max(i[1], curr[1])]
            else:
                res.append(curr)
                curr = i
        res.append(curr)
        return res