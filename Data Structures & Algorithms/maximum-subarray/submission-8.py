class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax=0
        res = float('-inf')
        for n in nums:
            curMax = max(curMax + n, n)
            res = max(curMax,res)
        return res