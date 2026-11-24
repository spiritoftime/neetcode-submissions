class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(num_open, num_close, combo):
            nonlocal res
            if num_open == n and num_close == n:
                res.append("".join(combo))
                return
            if num_open < n:
                backtrack(num_open + 1, num_close, combo + ["("])
            if num_close < n and num_close < num_open:
                backtrack(num_open, num_close + 1, combo + [")"])

        # TODO: Implement backtracking
        backtrack(0, 0, [])
        return res