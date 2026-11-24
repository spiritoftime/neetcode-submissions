class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[text1.length() + 1][text2.length() + 1];
        // // fill first col
        // for(int i = 0; i < text1.length(); i ++){
        //     char c1 = text1.charAt(i);
        //     if(c1 == text2.charAt(0)){
        //         dp[i][0] = 1;
        //     }
        // }
        // // fill first row
        // for(int i = 0; i < text2.length(); i ++){
        //     char c2 = text2.charAt(i);
        //     if(c2 == text1.charAt(0)){
        //         dp[0][i] = 1;
        //     }
        // }
        for(int i1 = 1; i1 <= text1.length(); i1++){
            for(int i2 = 1; i2<= text2.length(); i2++){
                char c1 = text1.charAt(i1-1);
                char c2 = text2.charAt(i2-1);

                // if current indices same char then increment largestLen
                dp[i1][i2] = c1 == c2 ? 
                // take the diagonal, dont need take all 3 sides
                dp[i1-1][i2-1] + 1 
                : 
                Math.max(
                    dp[i1-1][i2],
                    dp[i1][i2-1]
                );
            }
        }
        return dp[text1.length()][text2.length()];
    }
}
