class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {i:set() for i in range(9)}
        rows = {i:set() for i in range(9)}
        squares = {i:set() for i in range(9)}
        for r in rows:
            for c in cols:
                curr = board[r][c]
                if curr ==".":continue
                if curr in cols[c] or curr in rows[r] or curr in squares[(r//3)*3 + c//3]:
                    return False
                cols[c].add(curr)
                rows[r].add(curr)
                squares[(r//3)*3+c//3].add(curr)
        
        return True


        