class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = -1, len(matrix)
        # find row target is in
        while lo + 1 < hi:
            mid = (lo+hi)//2
            if matrix[mid][-1] >= target:
                hi = mid
            else: lo = mid
        # soln not in search space
        if hi == len(matrix):return False
        row = hi

        lo,hi = -1,len(matrix[row])
        while lo + 1 < hi:
            mid = (lo+hi)//2
            if matrix[row][mid] >= target:
                hi = mid
            else: lo = mid     
        if hi == len(matrix[row]) or matrix[row][hi] != target: return False
        return True