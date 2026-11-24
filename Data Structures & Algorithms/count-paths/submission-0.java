
class Solution {
    private HashMap<String, Integer> dp = new HashMap<>();
    public int dfs(int r, int c, int m, int n){
        String coordKey = r + "," + c;
        // if went out of bounds
        if(r == m || c == n){
            return 0;
        }
        // use the cached response
        if(dp.containsKey(coordKey)){
            return dp.get(coordKey);
        }
        // reached the end
        if(r == m -1 && c == n -1){
            dp.put(coordKey,
                dp.getOrDefault(coordKey,0) + 1
            );
            return dp.get(coordKey);
        }
        // move right
        return dfs(r+1,c,m,n) 
        // move down
        + dfs(r,c+1,m,n);
    }
    public int uniquePaths(int m, int n) {
        return dfs(0,0,m,n);
    }
}
