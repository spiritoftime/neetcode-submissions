class Solution:
    def jump(self, nums: List[int]) -> int:
        numJumps=0
        l,r=0,0
        furthest=0
        while r < len(nums):
            if furthest == len(nums)-1:return numJumps
            for i in range(l,r+1):
                furthest = max(furthest, nums[i] + i)
            l = r+1
            numJumps+=1
            r = furthest
            if furthest == len(nums)-1:return numJumps
        return numJumps
