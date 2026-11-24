class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 } # there is 1 subarray with prefix sum of 0

        for num in nums:
            curSum += num
            diff = curSum - k
            # is there a subarray i can form by removing a subarray of prefix sum diff
            # given curSum?
            res += prefixSums.get(diff, 0)
            # add curSum as current prefix sum to hm
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res