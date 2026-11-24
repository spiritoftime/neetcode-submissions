class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtrack(r,posDia, negDia, col, n, grid, numPlaced):
            if numPlaced == n:
                result = ["".join(grid[j]) for j in range(n)]
                res.append(result)
                return
            for c in range(n):
                if c in col or (r-c) in negDia or (r+c) in posDia: continue
                col.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                grid[r][c] = "Q"
                backtrack(r+1,posDia, negDia, col, n, grid, numPlaced+1)
                col.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                grid[r][c] = "."


        posDia,negDia, col = set(),set(),set()
        grid = [["." for i in range(n)] for j in range(n)]
        backtrack(0,posDia, negDia, col, n, grid, 0)
        return res