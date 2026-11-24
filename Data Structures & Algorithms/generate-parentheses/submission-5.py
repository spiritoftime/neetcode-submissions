class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(numOpen,numClose, combo):
            if numClose > numOpen or numClose > n or numOpen > n: return
            if numOpen == n and numClose == n:
                res.append("".join(combo))
                return
            backtrack(numOpen+1, numClose, combo + ["("])
            backtrack(numOpen, numClose+1, combo + [")"])

        backtrack(0, 0, [])
        return res