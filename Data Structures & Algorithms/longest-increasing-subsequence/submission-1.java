class Solution {
    // [3,5,7],target = 4
    public int binarySearch(ArrayList<Integer> seq, int target){
        int l = 0; 
        int r = seq.size()- 1;
        while(l <= r){
            int m = (l+r)/2;
            if(seq.get(m) == target){
                return m;
            }
            // increment left pointer
            else if(seq.get(m) < target){
                l = m+1;

            }
            else{
                r = m-1;

            }
        }
        return l; // Return the position where target should be inserted

    }
    public int lengthOfLIS(int[] nums) {
        ArrayList<Integer> seq = new ArrayList<>();
        seq.add(nums[0]);
        for(int i = 1; i < nums.length; i ++){
            int newNum = nums[i];
            // attempt to find it. if not it will find the number beside the newNum

            int numIndex = binarySearch(seq, newNum);
            // remove the existing number and replace it with the newNum

            if(numIndex < seq.size()){
                // replace existing number
                seq.set(numIndex, newNum);
            }
            // if binary search returns seq.size(), then the number is the largest number seen
            // outside of seq
            // eg: [1,2,3], 4
            else{
                seq.add(newNum);
            }

            
        }
        return seq.size();
    }
}
