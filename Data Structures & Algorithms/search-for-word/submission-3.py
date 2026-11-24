class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # start from the first letter
        possible = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    possible.append((r,c))
        def backtrack(currIndex,wordIndex):
            if currIndex[0] < 0 or currIndex[0] >= len(board) or currIndex[1] < 0 or currIndex[1] >= len(board[0]):
                return False
            if board[currIndex[0]][currIndex[1]] != word[wordIndex]:
                return False
            else:
                if wordIndex == len(word) - 1:
                    return True
            tmp = board[currIndex[0]][currIndex[1]]
            board[currIndex[0]][currIndex[1]] = 0
            for r,c in directions:
                res = backtrack((currIndex[0] + r, currIndex[1] + c),wordIndex+1)

                if res:
                    board[currIndex[0]][currIndex[1]] = tmp

                    return True
            board[currIndex[0]][currIndex[1]] = tmp

            return False


        for p in possible:
            res = backtrack(p,0)
            if res:
                return True
        return False

        