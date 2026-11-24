class Solution {
    public int maxSubArray(int[] nums) {
        int[] dp = new int[nums.length];
        // base case: last index subarray max subarray is just itself
        dp[nums.length-1] = nums[nums.length-1];
        for(int i = nums.length -2; i >=0; i--){
            dp[i] = 
            dp[i+1] < 0 ?
             nums[i] : 
             nums[i] + dp[i+1];
        }
        int largest = dp[nums.length-1];
        for(int n : dp){
            if(n > largest){
                largest = n;
            }
        }
        return largest;
    }
}
