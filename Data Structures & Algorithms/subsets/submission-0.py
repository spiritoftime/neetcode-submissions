class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtrack(combo,i):
            if i >= len(nums):
                return
            self.res.append(combo)
            for n in range(i+1,len(nums)):
                backtrack(combo + [nums[n]], n)

        backtrack([],-1)
        return self.res
            