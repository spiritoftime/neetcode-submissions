class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def backtrack(i,j, board, remainingWord):
            if not remainingWord: return True # traversed finish
            if i < 0 or j <0 or i >= len(board) or j >= len(board[0]): return False 
            if board[i][j] != remainingWord[0] or board[i][j] == "@":return False
            c = board[i][j]
            board[i][j] = '@'
            for x,y in directions:
                new_x = x + i
                new_y = y+j
                if backtrack(new_x, new_y, board,remainingWord[1:]):return True
            board[i][j] = c
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == word[0]:
                    if backtrack(i,j,board, word): return True
        return False