
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(board), len(board[0])

        def dfs(i, j):
            board[i][j] = "Marked"

            for x, y in directions:
                ix, iy = i+x, j+y

                if (0 <= ix < m and 0 <= iy < n
                    and board[ix][iy] == "O"):
                    dfs(ix, iy)

        # DFS from boundary cells
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == "O":
                        dfs(i, j)

        # Restore boundary-connected zeros; capture the rest
        for i in range(m):
            for j in range(n):
                if board[i][j] == "Marked":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
