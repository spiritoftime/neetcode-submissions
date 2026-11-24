class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """start from the border. all Os that the border can reach cannot be solved."""
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(i, j):
            if (
                i < 0
                or j < 0
                or i >= len(board)
                or j >= len(board[0])
                or board[i][j] != "O"
            ):
                return
            board[i][j] = "T"
            for x, y in directions:
                dfs(i + x, j + y)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"