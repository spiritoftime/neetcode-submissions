class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(r,c):
            d = [(0,1),(0,-1),(1,0),(-1,0)]
            if r <0 or c<0 or r>=len(board) or c>= len(board[0]) or board[r][c] != "O":
                return
            board[r][c] = "T"
            for r1,c1 in d:
                dfs(r+r1,c+c1)
        for r in range(len(board)):
            dfs(r,0)
            dfs(r,len(board[0])-1)
        for c in range(len(board[0])):
            dfs(0,c)
            dfs(len(board)-1,c)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

        