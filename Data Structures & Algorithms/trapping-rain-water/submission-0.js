class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        if (!height || height.length === 0) {
            return 0;
        }
        let l = 0
        let r = height.length -1
        let maxL = height[l]
        let maxR = height[r]
        let maxWater = 0
        // keep track of the largest boundary
        // then we can get the area collected
        // at each index.
        while (l < r){
            if(height[l] < height[r]) {
                l +=1
                maxL = Math.max(maxL, height[l])
                maxWater += maxL - height[l]
            }
            else {
                r-=1
                maxR = Math.max(maxR, height[r])
                maxWater += maxR - height[r]
            }
        }
        return maxWater
    }
}