
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        def canMerge(i1, i2):
            if (
                i1[0] <= i2[0] <= i1[1]
            ):  # if start of 2nd is within the previous interval
                return True
            return False

        intervals.sort(key=lambda x: x[0])  # sort ascending by start time
        res = []
        curr = intervals[0]
        for i in range(len(intervals)):
            if canMerge(curr, intervals[i]):
                curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
            else:
                res.append(curr)
                curr = intervals[i]
        res.append(curr)
        return res