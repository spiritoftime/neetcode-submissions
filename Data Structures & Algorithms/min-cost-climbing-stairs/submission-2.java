class Solution {
    public int minCostClimbingStairs(int[] cost) {
        // subproblem: from here, do i jump 1 or 2 steps?
        // last 2 steps are the base cases. at last step, just jump 1.
        // 2nd last -> jump 2.
        int[] dp = new int[cost.length];
        // base cases - last and 2nd last step
        dp[cost.length -1] = cost[cost.length - 1];
        dp[cost.length -2] = cost[cost.length - 2];
        // reverse loop starting from 3rd last step.
        for(int i = cost.length - 3; i >= 0; i --){
            // after paying the cost of current step,
            // do i want to jump 1 or 2 steps?
            dp[i] =cost[i] + Math.min(
                dp[i + 1],
                dp[i+2]
            );

        }
        return Math.min(dp[0],dp[1]);


    }
}
