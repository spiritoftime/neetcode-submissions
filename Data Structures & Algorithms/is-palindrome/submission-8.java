class Solution {
    public boolean isPalindrome(String s) {
        // remove all case sensitivty
        String lowerS = s.toLowerCase();
        int len = s.length();
        int l = 0;
        int r = len - 1;
        //  two pointer condition
        while (l <= r){
            char lc = lowerS.charAt(l);
            char rc = lowerS.charAt(r);
           // check if nonalphanumeric character
            if(!Character.isLetterOrDigit(lc)){
                l += 1;
                continue;
            }
            if(!Character.isLetterOrDigit(rc)){
                r -= 1;
                continue;
            }
            // check if same characters
            if(lc != rc){
                return false;
            }
 
            // valid case just continue
            l+=1;
            r-=1;

        }
        // at the end return true
        return true;
    }
}
