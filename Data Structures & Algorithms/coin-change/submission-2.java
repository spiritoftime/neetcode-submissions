class Solution {
    public int coinChange(int[] coins, int amount) {
        
        int[] memo = new int[amount+1];
        // base case - 0 coins needed when there is no coins to choose from
        // by default java initialize with 0
        // fill the other indexes with large number 
        for(int i =1; i < memo.length; i++){
            memo[i] = Integer.MAX_VALUE;
        }
        for(int a = 1; a < memo.length; a++){
            // for every given amount, attempt to add every single coin
            for(int c: coins){
                if(a - c >= 0
                // need this, because later on you do memo[a-c] + 1
                // when memo[a-c] is Integer.MAX_VALUE, adding 1 causes
                // integer overflow which causes answer to be wrong.
                // alternatively dont use Integer.MAX_VALUE
                && memo[a-c] != Integer.MAX_VALUE
                ){
                    memo[a] = Math.min(
                        // dont take this coin
                        memo[a],
                        // take this coin to make up amount
                    memo[a-c] + 1);
                }
            }
        }
        return memo[amount] == Integer.MAX_VALUE ? -1: memo[amount];

    }
}
