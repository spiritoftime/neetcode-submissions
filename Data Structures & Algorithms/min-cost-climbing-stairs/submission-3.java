class Solution {
    // top down: recursion with memoization
    // start from final state - which is the last index
    // returns the final min cost of the recursion
    public int recurse(int i, int[] memo, int[] cost){
        // computed this before - default int[] initialization is 0 cost
        if(memo[i] != 0){
            return memo[i];
        }
        // the first 2 steps - base case
        if(i == 0 || i == 1){
            // store the state
            memo[i] = cost[i];
            return memo[i];
        }
        // compute and store the state
        memo[i] = Math.min(recurse(i-1, memo, cost),
        recurse(i-2, memo, cost) ) + cost[i];
        // return the state upwards the stack trace
        return memo[i];

    }
    public int minCostClimbingStairs(int[] cost){
        // memo to store the computation results
        int[] memo = new int[cost.length];

        return Math.min(
            // the min cost lies either ending at the last stair (jump 1 from there)
            recurse(cost.length -1, memo, cost),
            // or ending at the 2nd last stair (then from there jump 2)
            recurse(cost.length -2, memo, cost)
        );

    }
    // bottom up: 
    // public int minCostClimbingStairs(int[] cost) {
    //     // subproblem: from here, do i jump 1 or 2 steps?
    //     // last 2 steps are the base cases. at last step, just jump 1.
    //     // 2nd last -> jump 2.
    //     int[] dp = new int[cost.length];
    //     // base cases - last and 2nd last step
    //     dp[cost.length -1] = cost[cost.length - 1];
    //     dp[cost.length -2] = cost[cost.length - 2];
    //     // reverse loop starting from 3rd last step.
    //     for(int i = cost.length - 3; i >= 0; i --){
    //         // after paying the cost of current step,
    //         // do i want to jump 1 or 2 steps?
    //         dp[i] =cost[i] + Math.min(
    //             dp[i + 1],
    //             dp[i+2]
    //         );

    //     }
    //     // you can choose to start at 1st or 2nd step.
    //     return Math.min(dp[0],dp[1]);


    // }
}
