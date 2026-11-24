class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # at every step, we can include or not include the curr num to our subset
        target = sum(nums) /2
        if int(target) != target: return False # odd number, no partition
        dp = [] # take curr num, dont take curr num
        def dfs(i, subset, total):
            if total == target: return True
            if total > target or i >= len(nums): return False
            include = dfs(i+1, subset + [nums[i]], total + nums[i])
            if include: return True
            exclude = dfs(i+1, subset, total)
            if exclude: return True
            return False
        return dfs(0, [], 0)
            
        