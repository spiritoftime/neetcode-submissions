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
        l = 0
        r = len(matrix[rowToCheck]) - 1
        row = matrix[rowToCheck]
        while l <=r:
            m = (l+r) // 2
            if row[m] == target:
                return True
            elif row[m] > target:
                r = m-1
            else:
                l = m+1
        return False 
