class Solution {
    public int longestConsecutive(int[] nums) {
        // use a hashset and index the nums
        // keep trying to get the next number
        HashSet<Integer> uniqueNums = new HashSet<>();
        for(int n:nums){
            uniqueNums.add(n);
        }
        int largestSeq = 0;
        for (int n : nums){
           int  currSeq = 1;
           int currNum = n;
           while (uniqueNums.contains(currNum+1)){
            currSeq += 1;
            currNum += 1;
           }
           largestSeq = Math.max(currSeq, largestSeq);
        }
        return largestSeq;
    }
}
