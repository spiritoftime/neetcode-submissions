class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtrack(combo):
            if len(combo) == len(nums):
                self.res.append(list(combo))
                return
            for curr in nums:
                if curr not in combo:
                    combo.append(curr)
                    backtrack(combo)
                    combo.pop()
        backtrack([])
        return self.res

        