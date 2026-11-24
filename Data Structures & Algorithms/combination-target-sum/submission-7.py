class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, subset, total):
            if total == target:
                res.append(list(subset))
                return
            if total > target: return

            for j in range(i, len(nums)):

                total += nums[j]
                subset.append(nums[j])
                backtrack(j, subset, total)
                total -= nums[j]
                subset.pop()
        backtrack(0, [], 0)
        return res
