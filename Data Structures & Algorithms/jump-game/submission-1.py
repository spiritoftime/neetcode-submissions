class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [1,2,0,1,0]
        # from every step, try to jump 
        # from (1,nums[i]) steps then try to reach end
        # res[i] is whether can reach end
        # res[-1] definitely is True
        res = [False] * len(nums)
        res[-1] = True
        for i in range(len(nums)-1,-1,-1):
            for j in  range(nums[i]+1):
                if i+j < len(res) and res[i+j]:
                    res[i] = True
                    break
        return res[0]