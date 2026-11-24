class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #determine which row to check
        rowToCheck = 0
        for r in range(len(matrix)-1):
            last = matrix[r][-1]
            first = matrix[r][0]
            if first <= target <= last:
                rowToCheck = r
                break
            else:
                rowToCheck = r+1
        # found the row to search
        l,r = 0, len(matrix[rowToCheck]) - 1
        while l <=r:
            m = (l+r) // 2
            if matrix[rowToCheck][m] == target: return True
            elif matrix[rowToCheck][m] > target: r=m-1
            else: l = m+1
        return False