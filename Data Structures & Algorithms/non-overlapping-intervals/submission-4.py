class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        def canMerge(i1,i2):
            return i1[1] > i2[0]
        st = [intervals[0]]
        res = 0
        for i in range(1, len(intervals)):
            if canMerge(st[-1], intervals[i]): 
                res += 1
                continue # keep the smallest end time interval

            else: st.append(intervals[i])
        return res