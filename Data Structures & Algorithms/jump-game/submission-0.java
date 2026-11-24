class Solution {
    public boolean canJump(int[] nums) {
        int destination = nums.length - 1;
        boolean[] memo = new boolean[nums.length];
        
        // last index base case: it can reach itself
        memo[nums.length - 1] = true;
        for(int i = nums.length - 2 ; i >= 0 ; i --){
            int jumpable = nums[i];
            // if from this position, it can reach destination
            if(i + jumpable >= destination){
                memo[i] = true;
            }
            // else, to reach destination it needs to jump to 
            // a position that can reach destination
            else{
                for(int j = 1 + i; j <= jumpable + i
                 && j < memo.length; j ++){
                    boolean jumpTo = memo[j];
                    if(jumpTo == true){
                        memo[i] = true;
                    }
                }
            }
        }
        // return the result at first index.
        return memo[0];

    }
}
