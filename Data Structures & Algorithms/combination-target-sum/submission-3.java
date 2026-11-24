class Solution {
    private List<List<Integer>> combos = new ArrayList<>();

    public void backtrack(int[] nums, 
    int target,List<Integer> state, int i) {
        // valid combo
        if(target == 0){
            // create a new copy of state so that reference wont point to 
            // mutable state
            combos.add(new ArrayList<>(state));
            return;
        }
        // 
        if(target < 0 || i >= nums.length){
            return;
        }
        // explore the possibility of the combo containing current node
        state.add(nums[i]);
        backtrack(nums,target - nums[i], state, i);
        // after exploration, remove the number 
        // so that we can explore possibility of combo not containing current node
        state.remove(state.size() - 1);
        backtrack(nums,target,state, i+1);
    }

    
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<Integer> state = new ArrayList<>();
        backtrack(nums,target,state, 0);
        return combos;
    }
}
