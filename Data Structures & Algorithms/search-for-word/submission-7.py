class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # start from the first letter
        possible = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def backtrack(r,c,wordIndex):
            if r < 0 or c <0 or r >= len(board) or c>= len(board[0]):
                return False
            curr = board[r][c]

            if wordIndex == len(word) -1 and curr == word[-1]:
                return True
            if curr != word[wordIndex]:
                return False
            board[r][c] = 0
            for r1,c1 in directions:
                res = backtrack(r+r1,c+c1,wordIndex+1)
                if res:
                    board[r][c] = curr

                    return True
            board[r][c] = curr

            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if backtrack(r,c,0):
                        return True
        return False


        