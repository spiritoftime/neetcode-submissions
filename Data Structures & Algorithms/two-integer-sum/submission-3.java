class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] out = {0,0};
        HashMap<Integer,Integer> hm = new HashMap<>();
        for( int i = 0; i < nums.length; i ++){
            int n = nums[i];
            //  there is the pairing number
            if(hm.containsKey(target - n)){
                out[0] = hm.get(target - n);
                out[1] = i;
                return out;
            }
            hm.put(n,i);
        }
        return out;
    }
}
