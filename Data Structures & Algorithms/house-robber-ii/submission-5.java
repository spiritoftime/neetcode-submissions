class Solution {
    public int robNonCircle(int[] nums){
        int[] dp  = new int[nums.length];
        dp[0] = nums[0];
        // rob only 1 if theres only 2 house
        dp[1] = Math.max(nums[0], nums[1]);
        for(int i = 2; i < nums.length; i ++){
            dp[i] = Math.max(
                // rob current + all previous non adjacents
                dp[i-2] + nums[i],
                // dont rob the current house
                dp[i-1]
            ); 
        }

        return dp[nums.length-1];
        
    }
    public int rob(int[] nums) {
        // exception handling 
        if(nums.length == 0){
            return 0;
        }
        // cannot do if (nums.length <=2) return robNonCircle(nums)
        // this will result in IndexOutOfBoundsException, since
        // we are indexing dp[1] and othbers at rob NonCircle
        if(nums.length == 1){
            return nums[0];
        }
        if(nums.length == 2){
            return Math.max(nums[0],nums[1]);
        }
        // you can only choose to rob from 1st index (2nd house) to last house,
        // OR 1st house (0th index) to 2nd last house
        // this is so as to avoid the adjacent requirement.
        return Math.max(
            robNonCircle(
                // copyOfRange returns primitive array type
                // end range is exclusive, start range is inclusive.
                // 2nd to last
            Arrays.copyOfRange(nums,1,nums.length)
            ),
            robNonCircle(
            // 1st to 2nd last
            Arrays.copyOfRange(nums,0,nums.length - 1)
            )
        );
    }
}
