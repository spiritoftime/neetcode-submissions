class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0
        res = 0
        while l < r:
            currL, currR = height[l], height[r]
            # water will be able to flow down from the maximum height in one direction all the way down to the curr height.
            maxL, maxR = max(currL, maxL), max(currR, maxR)
            res += maxL - currL
            res += maxR - currR
            # if maxL is 4 and maxR is 5, the maximum amount of water contained in each step can only be 4 (the 5th ml will overflow out). thats why we only increment the smaller height.
            if currL < currR:
                l += 1
            else:
                r -= 1
        return res
