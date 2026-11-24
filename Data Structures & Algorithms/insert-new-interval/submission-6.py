class Solution:
    def binarySearch(self,intervals, newIntervalStart):
        # binary search to find where to insert newInterval so it is still sorted
        l,r = 0 , len(intervals) - 1
        while l <=r:
            m = (l+r) // 2
            if intervals[m][0] == newIntervalStart: return m
            elif intervals[m][0] > newIntervalStart: r=m-1
            else:l=m+1
        return l 
    def canMerge(self,i1, i2):
        if i1[1] >= i2[0]: return True
        return False

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx_insert = self.binarySearch(intervals, newInterval[0])
        intervals.insert(idx_insert, newInterval)
        #merge all the intervals
        st = [intervals[0]]
        for i in range(1, len(intervals)):
            if self.canMerge(st[-1], intervals[i]):
                top = st.pop()
                st.append([min(top[0], intervals[i][0]) , max(intervals[i][1], top[1]) ])
            else:
                st.append(intervals[i])
        return st
