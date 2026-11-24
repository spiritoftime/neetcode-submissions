
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # TODO: Implement backtracking
        res = []

        def backtrack(combo, choices):
            nonlocal res
            if not choices:
                res.append(combo.copy())
                return
            for i, n in enumerate(choices):
                choices.pop(i)
                backtrack(combo + [n], choices)
                choices.insert(i, n)

        backtrack([], nums)
        return res
