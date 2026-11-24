
class Solution {
    private List<List<Integer>> res = new ArrayList<>();

    public void backtrack(int start, int[] nums, List<Integer> ls) {
        res.add(new ArrayList<>(ls)); // Add a copy of the current subset

        for (int j = start; j < nums.length; j++) {
            ls.add(nums[j]);          // Include nums[j]
            backtrack(j + 1, nums, ls); // Move to the next element
            ls.remove(ls.size() - 1); // Backtrack (remove the last added element)
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        backtrack(0, nums, new ArrayList<>());
        return res;
    }
}
