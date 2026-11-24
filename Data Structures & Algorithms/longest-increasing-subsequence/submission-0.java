class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        // memo[i][0] stores nums[i], memo[i][1] stores the LIS length at index i
        int[][] memo = new int[n][2];

        // Initialize memo array: Each element is its own LIS of length 1
        for (int i = 0; i < n; i++) {
            memo[i][0] = nums[i]; // Store the number
            memo[i][1] = 1;       // Initial length of LIS ending at index i
        }

        // Start processing from the back of the array
        for (int i = n - 2; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                // Check if nums[i] can be followed by nums[j]
                if (nums[i] < nums[j]) {
                    // Update LIS length for memo[i][1] if a longer sequence is found
                    memo[i][1] = Math.max(memo[i][1], memo[j][1] + 1);
                }
            }
        }

        // Find the maximum LIS length from the memo array
        int largest = 0;
        for (int[] pair : memo) {
            largest = Math.max(largest, pair[1]);
        }

        return largest;
    }
}
