class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            cnt = 1
            tmp = n+1
            while tmp in nums:
                cnt +=1 
                tmp += 1
            res  = max(res,cnt)
        return res
