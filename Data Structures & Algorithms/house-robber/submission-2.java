class Solution {
    public int rob(int[] nums) {
        
        // forward approach
        // base cases : 1st and 2nd house - number of each other
        int[] dp = new int[nums.length];

        for(int i = 0; i < dp.length; i ++){
            // base cases 1st and 2nd house
            if ( i == 0){
                // they can only rob one house, since they are both
                // adjacent to one another
                dp[i] = nums[i];
            }
            else if (i==1) {
                dp[i] = Math.max(nums[i],nums[i-1]);
            }
            else{
                dp[i] = Math.max(
                    // choose to rob current house and non neighbour
                    dp[i-2] + nums[i],
                    // choose to skip
                    dp[i-1]
                );
            }

        }
        // if there is only 2 houses, 
        // choose to either rob first or second house.
        if(dp.length == 2){
            return Math.max(dp[0],dp[1]);
        }
        //  return the maximum
        return dp[nums.length - 1];
    }
}
