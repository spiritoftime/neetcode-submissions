
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(num_open, num_close, combo):
            nonlocal res
            if num_close > num_open or num_open > n or num_close > n:
                return
            if num_open == n and num_close == n:
                res.append("".join(combo))
                return
            backtrack(num_open + 1, num_close, combo + ["("])
            backtrack(num_open, num_close + 1, combo + [")"])

        # TODO: Implement backtracking
        backtrack(0, 0, [])
        return res