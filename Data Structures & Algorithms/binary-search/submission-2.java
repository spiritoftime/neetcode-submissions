class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        while (l <= r){
            // java auto removes decimal (not round up or down).
            // eg: 7/2 = 3.5. remove the .5 = 3
            int m = (l+r) / 2; 
            int middleNum = nums[m];
            if(middleNum == target){
                return m;
            } 
            // increment left pointer, which increases the middle number
            // since it is sorted in ascending order.
            else if(middleNum < target){
                l = m+ 1;
            }
            else{
                r = m- 1;
            }
        }
        // what if the target is not in nums??
        // try working out with 
        // nums = [-1,0,2,4,6,8], target = 5
        return -1;
    }
}
