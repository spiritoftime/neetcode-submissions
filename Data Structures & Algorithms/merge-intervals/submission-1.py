class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()

        def canMerge(i1, i2):
            if i1[1] >= i2[0]:return True
            return False
        st = [intervals[0]]
        for i in range(1,len(intervals)):
            if canMerge(st[-1], intervals[i]):
                top = st.pop()
                st.append([ top[0] , max(intervals[i][1], top[1])])
            else:
                st.append(intervals[i])
        return st