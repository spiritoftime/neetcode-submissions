class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        res,maxL,maxR = 0,0,0
        while l < r:
            maxR = max(height[r],maxR)
            maxL = max(height[l],maxL)
            if height[r] < maxR: res += maxR-height[r]
            if height[l] < maxL: res += maxL-height[l]
            if height[l] < height[r]: l+=1
            else:r-=1
        return res
