class Solution {
    public int countSubstrings(String s) {
        boolean[][] dp = new boolean[s.length()][s.length()];
        int res = 0;
        // single char is palindome
        for(int i = 0; i < s.length(); i ++){
            dp[i][i] = true;
            res +=1;
        }
        // double char need to check same chars
        for (int start = 0; start < s.length() - 1; start ++){
            dp[start][start + 1] = s.charAt(start) == s.charAt(start+1);
            if(dp[start][start+1] == true){
                res +=1;

            }
        }
        // finally, we loop through the 3 char string and more
        for(int length = 3; length <= s.length(); length ++){
            for (int start = 0;
                    start <= s.length() - length; start ++){
                        int end = start + length - 1;
                        dp[start][end] = s.charAt(start) == s.charAt(end)
                        && dp[start+1][end-1];
                        if(dp[start][end] == true){
                                        res +=1;

                                    }
                    }
        }
        return res;
    }
}
