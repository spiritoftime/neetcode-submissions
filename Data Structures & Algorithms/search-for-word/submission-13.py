class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited= set()
        def backtrack(i,j, board, remainingWord):
            if not remainingWord: return True # traversed finish
            if i < 0 or j <0 or i >= len(board) or j >= len(board[0]): return False 
            if board[i][j] != remainingWord[0] or (i,j) in visited:return False
            visited.add((i,j))
            for x,y in directions:
                new_x = x + i
                new_y = y+j
                if backtrack(new_x, new_y, board,remainingWord[1:]):return True
            visited.remove((i,j))
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == word[0]:
                    if backtrack(i,j,board, word): return True
        return False