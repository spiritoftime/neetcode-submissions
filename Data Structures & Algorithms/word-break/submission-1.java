class Solution {
    private HashMap<Integer, Boolean> memo = new HashMap<>();
    public boolean dfs(String s, List<String> wordDict, int currIndex){
        if (memo.containsKey(currIndex)){
            return memo.get(currIndex);
        }
        if(currIndex == s.length()) return true;
        String substr= "";
        for(int i = currIndex; i < s.length(); i ++){
            substr += String.valueOf(s.charAt(i));
            if(wordDict.contains(substr)){
                if(dfs(s,wordDict, i+1)){
                    memo.put(i, true);
                    return true;
                }
            }

        }
        memo.put(currIndex, false);
        return false;
        
    }
    public boolean wordBreak(String s, List<String> wordDict) {
        return dfs(s,wordDict,0);
    }
}
