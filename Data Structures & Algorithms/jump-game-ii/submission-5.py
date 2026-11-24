class Solution:
    def jump(self, nums: List[int]) -> int:
        numJumps=0
        l,r=0,0
        furthest=0
        while r < len(nums)-1:
            for i in range(l,r+1):
                furthest = max(furthest, nums[i] + i)
            l = r+1
            numJumps+=1
            r = furthest
        return numJumps
