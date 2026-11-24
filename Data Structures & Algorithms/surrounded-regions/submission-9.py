class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # border cells can never be flipped. so we start from border cells, and try
        # to infect O cells. infected ones can never be flipped
        directions = [(0,1),(1,0), (-1,0), (0,-1)]
        ROWS,COLS = len(board), len(board[0])
        def dfs(i,j):
            if i < 0 or j <0 or i >= ROWS or j >= COLS :
                return
            if board[i][j]== "X" or board[i][j] == "T" : return
            board[i][j] = "T"
            for r,c in directions:
                dfs(i+r,j+c)

            
        for r in range(ROWS):
            dfs(r,0)
            dfs(r,COLS-1)
        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1, c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
                    
