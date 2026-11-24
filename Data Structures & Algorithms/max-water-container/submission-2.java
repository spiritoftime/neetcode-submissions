class Solution {
    public int maxArea(int[] heights) {
        int maxArea = 0;
        int l = 0;
        int r = heights.length - 1;

        while (l < r){
            int minHeight = Math.min(heights[l],heights[r]);
            int currentArea = (r-l) * minHeight ;
            maxArea = Math.max(currentArea,maxArea);
            if(heights[l] == minHeight){
                l+=1;
            }
            else{
                r-=1;
            }
        }
        return maxArea;
    }
}
