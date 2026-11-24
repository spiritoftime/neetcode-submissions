class Solution:
    def permute(self, nums):
        res = []
        def backtrack(combo):
            if len(combo) == len(nums):
                res.append(list(combo))
                return
            for num in nums:
                if num not in combo:
                    combo.append(num)
                    backtrack(combo)
                    combo.pop()
        backtrack([])
        return res