class Solution {
    // uses endIndex inclusive.
    public String updateLongestString(String returnString,
    int startIndex, int endIndex, String s){
        // if the current returnString's length is longer, you need not update
        // it.
        if(returnString.length() >= 
        // length of the potential new string
        (endIndex - startIndex + 1)
        ){
            return returnString;
        }
        // update returnString
        return s.substring(startIndex, endIndex + 1);
    }
    public String longestPalindrome(String s) {
        String returnString = String.valueOf(s.charAt(0));
        // initialise the memo - a 2-dimensional array
        // where rowIndex is the startIndex,
        // and colIndex is the endIndex. stores whether a string
        // from startIndex to endIndex(inclusive) is a palindrome.
        boolean[][] memo = new boolean[s.length()][s.length()];
        // BASE CASE - 1 character string
        for(int startIndex = 0; startIndex < s.length(); startIndex ++){
            // each string with only 1 character is a palindrome.
            memo[startIndex][startIndex] = true;
            // attempt to update longest string if true.
            returnString = 
            updateLongestString(returnString, startIndex, startIndex,s);
        }
        // 2nd base case - 2 character string.
        // start starts from first to 2nd last character.
        for(int startIndex = 0; startIndex < s.length() - 1; startIndex ++){
            int endIndex = startIndex + 1;
            char startChar = s.charAt(startIndex);
            char endChar = s.charAt(endIndex);
            if(startChar == endChar){
            // if they are equal, the string with 2 chars
            // is a palindrome.
                memo[startIndex][endIndex] = true;
            // attempt to update longest string if true.
            returnString = 
            updateLongestString(returnString, startIndex, endIndex,s);
            }
            else{
                memo[startIndex][endIndex] = false;

            }
        }
        // now, we are ready to process the subproblems.
        // process 3 character string onwards
        for (int length = 3; length <= s.length(); length ++){
            for(int startIndex = 0; startIndex <= s.length() - length;
            startIndex ++){
                int endIndex = startIndex + length - 1;
                char startChar = s.charAt(startIndex);
                char endChar = s.charAt(endIndex);
                memo[startIndex][endIndex] = 
                // the outer characters need to be the same
                (startChar == endChar) 
                &&
                // the inner characters need to be the same
                memo[startIndex+1][endIndex-1];
                // attempt to update longest string if true.
                if(memo[startIndex][endIndex]){
                    returnString = 
                    updateLongestString(returnString, startIndex, endIndex,s);
                }

            }
        }


        return returnString;

    }
}
