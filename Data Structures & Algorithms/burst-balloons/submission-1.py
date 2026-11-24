class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        # at every balloon, try to pop it last.
        def dfs(l,r):
            if l >r:return 0
            if (l,r) in cache: return cache[(l,r)]
            for m in range(l,r+1):
                earnedCoins = nums[m] * nums[l-1] * nums[r+1]
                cache[(l,r)] = max(earnedCoins + dfs(l,m-1) + dfs(m+1,r),cache.get((l,r),0) )
            return cache[(l,r)]
        return dfs(1,len(nums) - 2)
                