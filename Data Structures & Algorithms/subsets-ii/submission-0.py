class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        def backtrack(combo,i):
            self.res.append(list(combo))
            for n in range(i+1,len(nums)):
                if n > i + 1 and nums[n] == nums[n-1]:
                    continue
                combo.append(nums[n])
                backtrack(combo, n)
                combo.pop()
        backtrack([],-1)
        return self.res
        