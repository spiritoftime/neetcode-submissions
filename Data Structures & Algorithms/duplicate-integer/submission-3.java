class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> uniqueNums = new HashSet<>();
        for (int i: nums){
            if(uniqueNums.contains(i)){
                return true;
            }
            uniqueNums.add(i);
        }
        return false;
    }
}
