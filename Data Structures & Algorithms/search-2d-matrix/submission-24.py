class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # minimization problem
        # find the row that target may be in
        lo,hi = -1,len(matrix)
        while lo +1 < hi:
            m = (lo+hi) // 2
            if matrix[m][-1] >= target: hi = m
            else: lo = m
        if hi == len(matrix): return False
        # hi is the first row where matrix[hi][0] >= target
        r = hi
        # find the column that target may be in
        lo,hi = -1,len(matrix[r])
        while lo +1 < hi:
            m = (lo+hi) // 2
            if matrix[r][m] >= target: hi = m
            else: lo = m
        if hi == len(matrix[r]) or matrix[r][hi] != target:return False
        return True

