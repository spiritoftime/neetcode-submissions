class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[text1.length()][text2.length()];
        dp[0][0] = text1.charAt(0) == text2.charAt(0) ? 1 :0;
        // fill first col
        for(int i = 1; i < text1.length(); i ++){
            char c1 = text1.charAt(i);
            dp[i][0] = text2.charAt(0) == c1 ? 1 : dp[i-1][0];

        }
        // fill first row
        for(int i = 1; i < text2.length(); i ++){
            char c2 = text2.charAt(i);
            dp[0][i] = text1.charAt(0) == c2 ? 1 : dp[0][i-1];
        }

        for(int i1 = 1; i1 < text1.length(); i1++){
            for(int i2 = 1; i2< text2.length(); i2++){
                char c1 = text1.charAt(i1);
                char c2 = text2.charAt(i2);
                dp[i1][i2] = 
                    // same char 
                    c1 == c2? 1 + dp[i1-1][i2-1] :
                    Math.max(
                        dp[i1-1][i2],
                        dp[i1][i2-1]
                    );
            }
        }
        return dp[text1.length()- 1][text2.length()- 1];
    }
}
