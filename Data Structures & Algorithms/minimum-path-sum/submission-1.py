class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])
        prev = [float('inf') for i in range(c + 1)]
        prev[1] = 0  # the top
        for i in range(1,r+1):
            curr = [float('inf') for i in range(c + 1)]
            for j in range(1,c+1):
                # from top and left + curr
                curr[j] = min(prev[j], curr[j-1]) + grid[i-1][j-1]
            prev=curr
        return curr[-1]