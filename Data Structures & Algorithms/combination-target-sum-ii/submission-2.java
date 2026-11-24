

class Solution {
    private List<List<Integer>> res;
    
    public void dfs(int[] candidates, int target, List<Integer> combo, int currSum, int currIdx) {
        if (currSum == target) {
            res.add(new ArrayList<>(combo));
            return;
        }
        
        for (int i = currIdx + 1; i < candidates.length; i++) {
            // Skip duplicates to avoid repeated combinations
            if (i > currIdx + 1 && candidates[i] == candidates[i - 1]) continue;
            
            int n = candidates[i];
            // If the sum exceeds target, stop exploring further
            if (currSum + n > target) return;
            
            combo.add(n);
            dfs(candidates, target, combo, currSum + n, i);
            combo.remove(combo.size() - 1);
        }
    }
    
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        res = new ArrayList<>();
        Arrays.sort(candidates); // Sorting helps with duplicate skipping
        dfs(candidates, target, new ArrayList<>(), 0, -1);
        return res;
    }
}
