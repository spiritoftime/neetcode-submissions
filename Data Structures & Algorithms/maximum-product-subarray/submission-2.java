class Solution {
    public int maxProduct(int[] nums) {
        int currMin = nums[0];
        int currMax = nums[0];
        int globalMax = nums[0];
        for (int i = 1; i < nums.length; i ++){
            int tmp = currMin;
            currMin = Math.min(
                Math.min(
                currMin * nums[i],
                nums[i]
            ), currMax * nums[i]);

            currMax = Math.max(
                Math.max(
                    tmp * nums[i],
                    currMax * nums[i]
                ), nums[i]
            );
            globalMax = Math.max(currMax, globalMax);

        }
        return globalMax;
    }
}
