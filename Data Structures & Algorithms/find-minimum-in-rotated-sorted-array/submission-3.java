class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        while (l <=r){
            int m = (l+r) / 2;
            int middleNum = nums[m];



            // decrement rightward pointer if middleNum is more than r
            // you want to go towards the sorted side (which means
            // minimum is to the right.)
            if (middleNum > nums[r]){
                l = m+1;
            } 
            // this cannot be first condition
            // if it is unsorted array, it will throw
            // IndexOutOfBoundsException because you are doing m-1
            else if(m > 0 && middleNum < nums[m-1]){
                return middleNum;
            }
            // let the else handle the rest~
            else{
                r = m-1;
            }
        }

        // this will trigger if unsorted array
        // [1,2,3,4]
        // l = 0, r = 3. m = 1. shift r to m-1 = 0.
        // the else if condition cannot trigger, else there will be
        // IndexOutOfBoundsException.
        // hence you need to return outside while loop

        return nums[l];
    }
}
