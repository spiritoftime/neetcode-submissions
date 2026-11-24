class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) -1
        lh,rh = 0,0
        res = 0
        while l < r:
            lh = max(height[l], lh)
            rh = max(height[r], rh)

            res += lh - height[l]
            res += rh - height[r]
            if lh < rh: l+=1
            else: r-=1
        return res