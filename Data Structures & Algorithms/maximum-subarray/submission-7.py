class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax,curMin = 0,0
        res = float('-inf')
        for n in nums:
            tmp = curMax
            curMax = max(curMax + n, curMin+n,n)
            curMin = min(curMin+n,n,tmp+n)
            res = max(curMax,res)
        return res