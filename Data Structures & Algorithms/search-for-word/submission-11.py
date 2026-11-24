class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # TODO: Implement DFS/backtracking
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def backtrack(i, j, k):

            # out of bounds
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[k]:
                return False
            if (i, j) in visited:
                return False
            # i and j is coords on the board, k is the index of the word to find now
            if k == len(word) - 1:
                return True
            # prevent going back to the previous steps which are used for previous indicies of the word
            visited.add((i, j))
            # current char in word found, now traverse the next steps to try to find subsequent ones.
            for x, y in directions:
                if backtrack(i + x, j + y, k + 1):
                    return True
            # remove state after backtracking
            visited.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == word[0]:
                    if backtrack(i, j, 0):
                        return True
        return False
