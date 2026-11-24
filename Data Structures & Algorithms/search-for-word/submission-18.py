class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def backtrack(r,c, i):
            if  r >= len(board) or c >= len(board[0]) or r <0 or c <0 or board[r][c] != word[i] or board[r][c] == "visited":
                return False
            if i == len(word) -1: return True
            tmp = board[r][c]
            board[r][c] = "visited!"
            for x,y in directions:
                new_r = r + x
                new_c = c+ y
                if backtrack(new_r,new_c, i+1): return True
            board[r][c] = tmp
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if word[0] == board[r][c]:
                    if backtrack(r,c,0): return True
        return False