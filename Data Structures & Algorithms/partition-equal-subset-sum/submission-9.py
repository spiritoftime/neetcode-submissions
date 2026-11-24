class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if int(target) != target: return False
        target = int(target)
        dp = [False for i in range(target+1)]
        dp[0] = True # possible to form subset with sum 0
        # for every number, is it possible to form a subset with total = number
        # with the curr num, or the curr num with any subset??
        for n in nums:
            # why n -1 and not -1? 
            # When j < n, j - n is negative. 
            # Python doesn't throw an error here — it wraps around and indexes from the end of the array, giving wrong results.
            for j in range(len(dp) -1, n - 1, -1):
                dp[j] = dp[j] or dp[j - n ]
        return dp[target]