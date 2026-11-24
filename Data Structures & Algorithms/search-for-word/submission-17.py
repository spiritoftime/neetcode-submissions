class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        def backtrack(r,c, i, visited):
            if (r,c) in visited or r >= len(board) or c >= len(board[0]) or r <0 or c <0 or board[r][c] != word[i]:
                return False
            if i == len(word) -1: return True
            visited.add((r,c))
            for x,y in directions:
                new_r = r + x
                new_c = c+ y
                if backtrack(new_r,new_c, i+1, visited): return True
            visited.remove((r,c))
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if word[0] == board[r][c]:
                    if backtrack(r,c,0, visited): return True
        return False