class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # nextSmaller needs to be len(heights) to indicate there is no nextSmaller
        # eg: [1,2,3,4,4] -> possible to do 1 *5 too as answer
        prevSmaller,nextSmaller = [-1] * len(heights), [len(heights)] * len(heights)
        st = []
        res = 0
        for i in range(len(heights)):
            # we want monotonically strict increasing, because everytime we get a smaller height
            # it means that the maxArea can no longer increase for previous indexes.
            # (curr height will limit the maxArea of all previous indexes)
            # we dont use >= because [3,3,3] and incoming 4 dont need pop yet
            # maxArea can still increase. [3,3,3] and incoming 2 is the issue
            while st and heights[st[-1]] > heights[i]:
                n = st.pop()
                res = max(res, (i -n +1) * heights[i])
                nextSmaller[n] = i
            if st:
                prevSmaller[i] = st[-1]
            st.append(i)
        for i in range(len(heights)):
            currentHeight = heights[i]
            width = nextSmaller[i] - prevSmaller[i] - 1
            res = max(res, currentHeight * width)
        
        return res